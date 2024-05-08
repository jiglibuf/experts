import re
import streamlit as st

from dao import BaseDAO
from replacements import Replacements

class DataInput:
    def __init__(self):
        self.kn_input_value = ""
        self.kc_input_value = ""
        self.kc_selected_value = ""
        self.fio_input_value = ""
        self.fio_representative_input_value = ""
        self.request_adress = ""
        self.num_incoming_input_value = ""
        self.request_date_value = None
        self.email = ""
        self.docname = ""
        self.required_fields = ['kn_input_value', 'fio_input_value', 'num_incoming_input_value', 'request_date_value']


    def get_input_values(self):
        self.kn_input_value = st.text_input("Введите Кадастровый номер", self.kn_input_value)
        self.kc_input_value = st.text_input("Введите Кадастровую стоимость указанную в обращении", self.kc_input_value)
        self.fio_input_value = st.text_input("ФИО или наименование Заявителя", self.fio_input_value)
        self.fio_representative_input_value = st.text_input("Фамилия, имя, отчество (последнее - при наличии) представителя заявителя", self.fio_representative_input_value)
        self.request_adress = st.text_input("Адрес заявителя", self.request_adress)
        self.num_incoming_input_value = st.text_input("Входящий номер", self.num_incoming_input_value)
        self.request_date_value = st.date_input("Дата поступления обращения", self.request_date_value)
        self.email = st.text_input("Почта", self.email)

        for field in self.required_fields:
            if getattr(self, field) == "":
                st.error(f"Поле '{field}' является обязательным!")
                st.stop()

    def update_replacements(self, replacements_obj:Replacements):
        # replacements_obj.update('<КадастровыйНомер>', self.kn_input_value)
        # replacements_obj.update('<КадастроваяСтоимостьОбращения>', self.kc_input_value.replace(' ', '').replace('.', ','))
        # replacements_obj.update('<АкутальнаяКС>', self.kc_selected_value)
        # replacements_obj.update('<ФИО>', self.fio_input_value)
        # replacements_obj.update('<Представитель>', self.fio_representative_input_value)
        # replacements_obj.update('<АдресЗаявителя>', self.request_adress)
        # replacements_obj.update('<НомерЗаявления>', self.num_request_input_value)
        # replacements_obj.update('<ДатаПоступленияЗаявления>', self.request_date_value.strftime('%d.%m.%Y'))
        replacements_obj.update_attributes(kn_input_value = self.kn_input_value)
        replacements_obj.update_attributes(kc_input_value = self.kc_input_value.replace(' ', '').replace('.', ','))
        replacements_obj.update_attributes(kc_selected_value=self.kc_selected_value + ('0' if len(self.kc_selected_value.split(',')[1]) == 1 else ''))
        replacements_obj.update_attributes(fio_input_value = re.sub(r'"(.*?)"', r'«\1»', self.fio_input_value) )
        replacements_obj.update_attributes(fio_representative_input_value = re.sub(r'"(.*?)"', r'«\1»', self.fio_representative_input_value))
        replacements_obj.update_attributes(request_adress = self.request_adress)
        replacements_obj.update_attributes(num_incoming_input_value = self.num_incoming_input_value)
        replacements_obj.update_attributes(request_date_value = self.request_date_value.strftime('%d.%m.%Y'))
        # replacements_obj.update('<Почта>', self.email)
        replacements_obj.update_attributes(email = self.email)
        replacements_obj.update_attributes(docname = self.docname)
        # replacements_obj.update_docname(self.docname)

    def get_selected_kc(self):
        selected_kc = st.selectbox('Выберите стоимость', BaseDAO.get_all_kc(self.kn_input_value))
        if selected_kc:
            self.kc_selected_value = str(selected_kc[0]).replace(' ', '').replace('.', ',')
            self.docname = str(selected_kc[1])

    def show_actual_kc(self):
        actual_kc = BaseDAO.get_actual_kc(self.kn_input_value)
        if actual_kc:
            st.markdown(f"<div style='margin:2rem; border: 2px solid #f63366; border-radius: 2rem; padding: 10px; color: #f63366;'>Акутальная кадастровая стоимость: {actual_kc}</div>", unsafe_allow_html=True)
    
   