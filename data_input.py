import streamlit as st

from dao import BaseDAO

class DataInput:
    def __init__(self):
        self.kn_input_value = ""
        self.kc_input_value = ""
        self.kc_selected_value = ""
        self.fio_input_value = ""
        self.num_request_input_value = ""
        self.request_date_value = None
        self.email = ""
        self.docname = ""
        self.required_fields = ['kn_input_value', 'fio_input_value', 'num_request_input_value', 'request_date_value']


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

    def update_replacements(self, replacements_obj):
        replacements_obj.update('<КадастровыйНомер>', self.kn_input_value)
        replacements_obj.update('<КадастроваяСтоимостьОбращения>', self.kc_input_value.replace(' ', '').replace('.', ','))
        replacements_obj.update('<АкутальнаяКС>', self.kc_selected_value)
        replacements_obj.update('<ФИО>', self.fio_input_value)
        replacements_obj.update('<НомерЗаявления>', self.num_request_input_value)
        replacements_obj.update('<ДатаПоступленияЗаявления>', self.request_date_value.strftime('%d.%m.%Y'))
        # replacements_obj.update('<Почта>', self.email)
        replacements_obj.update_email(self.email)
        replacements_obj.update_docname(self.docname)

    def get_selected_kc(self):
        selected_kc = st.selectbox('Выберите стоимость', BaseDAO.get_all_kc(self.kn_input_value))
        if selected_kc:
            self.kc_selected_value = str(selected_kc[0]).replace(' ', '').replace('.', ',')
            self.docname = str(selected_kc[1])

    def show_actual_kc(self):
        actual_kc = BaseDAO.get_actual_kc(self.kn_input_value)
        if actual_kc:
            st.markdown(f"<div style='margin:2rem; border: 2px solid #f63366; border-radius: 2rem; padding: 10px; color: #f63366;'>Акутальная кадастровая стоимость: {actual_kc}</div>", unsafe_allow_html=True)
    
   