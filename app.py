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
    # template_path = 'template.docx'
    # doc = Document(template_path)

    # Определяем обязательные поля

    # Создаем экземпляр класса Replacements
    replacements = Replacements()

    # Создаем экземпляр класса DataInput
    data_input = DataInput()
    data_input.get_input_values()
    data_input.get_selected_kc()
    # Получаем значения из Streamlit input
    data_input.show_actual_kc()

    # Обновляем значения replacements
    data_input.update_replacements(replacements)
    print(replacements.kc_selected_value)
    print(replacements.kn_input_value)
    # Создаем экземпляр класса DataProcessor
    data_excel_hoarder = ExcelHoarder(replacements)
    data_processor = DataProcessor(replacements)
 

    
    # Кнопка для замены данных в шаблоне
    if st.button("Заменить данные в шаблоне"):

        data_processor.update_replacements()

        # st.write(replacements.kn_input_value)

        data_excel_hoarder.update_replacements()

        replacements.replace_decimal_points()

        replacements_dict = replacements.as_dict()

        # st.write(replacements_dict)

        template_path = replacements_dict['<template_path>']

        doc = Document(template_path)

        replace_text(doc, replacements_dict)

        # Сохраняем измененный файл
        output_path = f'{template_path}_output.docx'

        doc.save(output_path)

        st.success("Данные успешно заменены в шаблоне!")

        # Добавляем кнопку для скачивания файла
        with open(output_path, "rb") as file:
            btn = st.download_button(
                label="Скачать файл",
                data=file,
                file_name=output_path,
                mime="application/octet-stream"
            )

    # Закрываем соединение с базой данных

if __name__ == "__main__":
    main()