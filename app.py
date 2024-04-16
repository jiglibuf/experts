from docx import Document
from data_processor import DataProcessor
from excel_hoarder import ExcelHoarder
from replacements import Replacements
from utils import replace_text, update_conditions
from dao import BaseDAO
from data_input import DataInput
import streamlit as st 




def main():
    # Открываем шаблонный файл
    template_path = 'template.docx'
    doc = Document(template_path)

    # Определяем обязательные поля
    required_fields = ['kn_input_value', 'fio_input_value', 'num_request_input_value', 'request_date_value']

    # Создаем экземпляр класса Replacements
    replacements = Replacements()

    # Создаем экземпляр класса DataInput
    data_input = DataInput(required_fields)
    data_input.get_input_values()
    data_input.get_selected_kc()
    # Получаем значения из Streamlit input
    data_input.show_actual_kc()

    # Обновляем значения replacements
    data_input.update_replacements(replacements)

    # Создаем экземпляр класса DataProcessor
    data_processor = DataProcessor(replacements)
    st.write(str(replacements.kn_input_value))
    st.write(replacements.conditions['<КадастровыйНомер>'])

    data_excel_hoarder = ExcelHoarder(replacements)
    
    # Кнопка для замены данных в шаблоне
    if st.button("Заменить данные в шаблоне"):
        data_processor.get_osnovanie()
        data_processor.process_p_2()
        data_processor.process_p_3()
        data_processor.process_p_4()
        # st.write(replacements.conditions['<Условие4.2>'])
        st.write(replacements.kn_input_value)
        data_excel_hoarder.update_replacements()
        replacements_dict = replacements.as_dict()
        replace_text(doc, replacements_dict)
        st.success("Данные успешно заменены в шаблоне!")
        # Сохраняем измененный файл
        doc.save('output.docx')

    # Закрываем соединение с базой данных

if __name__ == "__main__":
    main()