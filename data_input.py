import streamlit as st

from dao import BaseDAO
from utils import update_conditions

class DataInput:
    def __init__(self, required_fields=None):
        self.kn_input_value = ""
        self.kc_input_value = ""
        self.kc_selected_value = ""
        self.fio_input_value = ""
        self.num_request_input_value = ""
        self.request_date_value = None
        self.email = ""
        self.docname = ""
        self.osnovanie = None
        self.replacements = {}
        self.required_fields = required_fields if required_fields is not None else []

    def get_input_values(self):
        self.kn_input_value = st.text_input("Введите Кадастровый номер", self.kn_input_value)
        self.kc_input_value = st.text_input("Введите Кадастровую стоимость указанную в обращении", self.kc_input_value)
        self.fio_input_value = st.text_input("Введите ФИО п.1.3", self.fio_input_value)
        self.num_request_input_value = st.text_input("Номер завявления", self.num_request_input_value)
        self.request_date_value = st.date_input("Дата поступления обращения", self.request_date_value)
        self.email = st.text_input("Почта", self.email)

        for field in self.required_fields:
            if getattr(self, field) == "":
                st.error(f"Поле '{field}' является обязательным!")
                st.stop()

    def get_replacements_dict(self):
        self.replacements = {
            '<КадастровыйНомер>': self.kn_input_value,
            '<КадастроваяСтоимость>': self.kc_input_value.replace(' ','').replace('.',','),
            '<АкутальнаяКС>': self.kc_selected_value,
            '<ФИО>': self.fio_input_value,
            '<НомерЗаявления>': self.num_request_input_value,
            '<ДатаПоступленияЗаявления>': self.request_date_value.strftime('%d.%m.%Y'),
            '<Почта>': self.email
        }
        # return replacements
    def get_smth(self, **kwargs):
        return BaseDAO.get_smth(self.kn_input_value,**kwargs)
    
    def get_selected_kc(self):
        selected_kc = st.selectbox('Выберите стоимость', BaseDAO.get_all_kc(self.kn_input_value))
        if selected_kc:
            self.kc_selected_value = str(selected_kc[0]).replace('.',',')
            self.docname = str(selected_kc[1])
        #         def get_selected_kc(self):
        # selected_kc = st.selectbox('Выберите стоимость', BaseDAO.get_all_kc(self.kn_input_value))
        # if selected_kc:
        #     self.kc_input_value = str(selected_kc[0]).replace('.',',')
        #     if selected_kc == BaseDAO.get_all_kc(self.kn_input_value)[0]:
        #         st.markdown("<style>div[data-baseweb='select'] > div:first-child {background-color: #f63366;}</style>", unsafe_allow_html=True)
        #         st.markdown("<style>div[data-baseweb='select'] > div:first-child::after {content: 'АКТУАЛЬНЫЙ'; color: #green;;}</style>", unsafe_allow_html=True)
    def show_actual_kc(self):
        actual_kc = BaseDAO.get_actual_kc(self.kn_input_value)
        if actual_kc:
            st.markdown(f"<div style='margin:2rem; border: 2px solid #f63366; border-radius: 2rem; padding: 10px; color: #f63366;'>Акутальная кадастровая стоимость: {actual_kc}</div>", unsafe_allow_html=True)
    
    def get_p_3(self):
        if not self.replacements['<КадастроваяСтоимость>']:
                self.replacements = update_conditions(self.replacements, '<Условие3_1>')
        else:
            if self.replacements['<АкутальнаяКС>'] == self.replacements['<КадастроваяСтоимость>']:
                st.write('равны')
                st.write(self.replacements['<АкутальнаяКС>'], self.replacements['<КадастроваяСтоимость>'])
                self.replacements = update_conditions(self.replacements, '<Условие3_2>')
            else:
                st.write('не равны')
                st.write(self.replacements['<АкутальнаяКС>'], self.replacements['<КадастроваяСтоимость>'])
                self.replacements = update_conditions(self.replacements, '<Условие3_3>')

    def get_p_4(self):
        if self.osnovanie =='ГКО':
            self.replacements = update_conditions(self.replacements, '<Условие4.3_1>')
            self.replacements = update_conditions(self.replacements, '<Условие4.4>', anchor='Приказ Министерства имущественных и земельных отношений Камчатского края от 27.11.2023 № 42-Н «Об утверждении результатов определения кадастровой стоимости объектов недвижимости на территории Камчатского края»')
            self.replacements = update_conditions(self.replacements, '<Условие4.2>', anchor='01.01.2023')
            self.replacements = update_conditions(self.replacements, '<Условие4.5>', anchor='''Официальный сайт бюджетного учреждения (порядок получения сведений о кадастровой стоимости):
https://gko.kamgov.ru/ocenka2023.php''')
            
        if self.docname in ['(в соответствии ст.16 Федерального закона от 03.07.2016 N 237-ФЗ «О государственной кадастровой оценке»)']:
            self.replacements = update_conditions(self.replacements, '<Условие4.3_2>')
        if self.docname in ['(в соответствии ст.15 Федерального закона от 03.07.2016 N 237-ФЗ «О государственной кадастровой оценке»)']:
            self.replacements = update_conditions(self.replacements, '<Условие4.3_3>')
        if self.docname in ['О внесении изменений в приказ Министерства имущественных и земельных отношений Камчатского края от 12.11.2020 N 179 «Об утверждении результатов определения кадастровой стоимости объектов капитального строительства, земельных участков категорий земель населенных пунктов, земель промышленности, энергетики, транспорта, связи, радиовещания, телевидения, информатики, земель для обеспечения космической деятельности, земель обороны, безопасности и земель иного специального назначения, расположенных на территории Камчатского края»',
                    'О внесении изменений в приказ Министерства имущественных и земельных отношений Камчатского края от 26.10.2022 N П-39 «Об утверждении результатов определения кадастровой стоимости земельных участков на территории Камчатского края»',
                    'О внесении изменений в приказ Министерства имущественных и земельных отношений Камчатского края от 27.11.2023 N 42-Н «Об утверждении результатов определения кадастровой стоимости объектов недвижимости на территории Камчатского края»'
                    ]:
            self.replacements = update_conditions(self.replacements, '<Условие4.3_4>')
        if not self.docname:
            # тут нужно вывести сообщение об ошибке
            pass
    
    def get_p_2(self):
        if self.kc_selected_value == self.kc_input_value:
            self.replacements = update_conditions(self.replacements, '<Условие2_1>')
        else:
            self.replacements = update_conditions(self.replacements, '<Условие2_2>')
    
    def get_osnovanie(self):
        if self.docname in ['Об утверждении результатов определения кадастровой стоимости зданий, помещений, сооружений, объектов незавершенного строительства, машино-мест на территории Камчатского края',
                    'Об утверждении результатов определения кадастровой стоимости объектов капитального строительства, земельных участков категорий земель населенных пунктов, земель промышленности, энергетики, транспорта, связи, радиовещания, телевидения, информатики, земель для обеспечения космической деятельности, земель обороны, безопасности и земель иного специального назначения, расположенных на территории Камчатского края',
                    'Об утверждении результатов определения кадастровой стоимости земельных участков категории земель сельскохозяйственного назначения, расположенных на территории Камчатского края',
                    'Об утверждении результатов определения кадастровой стоимости земельных участков на территории Камчатского края',
                    'Об утверждении результатов определения кадастровой стоимости зданий, помещений, сооружений, объектов незавершенного строительства, машино-мест на территории Камчатского края'
                    ]:
            self.osnovanie = 'ГКО'
            
        if self.docname in ['(в соответствии ст.16 Федерального закона от 03.07.2016 N 237-ФЗ «О государственной кадастровой оценке»)']:
            self.osnovanie = 'ст.16'
            
        if self.docname in ['(в соответствии ст.15 Федерального закона от 03.07.2016 N 237-ФЗ «О государственной кадастровой оценке»)']:
            self.osnovanie = 'ст.15'

        if self.docname in ['О внесении изменений в приказ Министерства имущественных и земельных отношений Камчатского края от 12.11.2020 N 179 «Об утверждении результатов определения кадастровой стоимости объектов капитального строительства, земельных участков категорий земель населенных пунктов, земель промышленности, энергетики, транспорта, связи, радиовещания, телевидения, информатики, земель для обеспечения космической деятельности, земель обороны, безопасности и земель иного специального назначения, расположенных на территории Камчатского края»',
                    'О внесении изменений в приказ Министерства имущественных и земельных отношений Камчатского края от 26.10.2022 N П-39 «Об утверждении результатов определения кадастровой стоимости земельных участков на территории Камчатского края»',
                    'О внесении изменений в приказ Министерства имущественных и земельных отношений Камчатского края от 27.11.2023 N 42-Н «Об утверждении результатов определения кадастровой стоимости объектов недвижимости на территории Камчатского края»'
                    ]:
            self.osnovanie = 'исправление ошибок'

        if not self.docname:
            # тут нужно вывести сообщение об ошибке
            pass