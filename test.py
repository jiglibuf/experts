from docx import Document
from docx.shared import Inches

def replace_text(doc, old_text, new_text):
    for paragraph in doc.paragraphs:
        if old_text in paragraph.text:
            paragraph.text = paragraph.text.replace(old_text, new_text)
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                if old_text in cell.text:
                    cell.text = cell.text.replace(old_text, new_text)

def main():
    # Открываем шаблонный файл
    template_path = 'шаблон.docx'
    doc = Document(template_path)

    # Заменяем данные в шаблоне
    replace_text(doc, 'OLD_TEXT', 'Соси')
    # Можно добавить сколько угодно таких замен

    # Сохраняем измененный файл
    doc.save('output.docx')

if __name__ == "__main__":
    main()
# import streamlit as st
# from docx import Document
# import datetime
# from utils import replace_text

# def main():
#     # Открываем шаблонный файл
#     template_path = 'template.docx'
#     doc = Document(template_path)

#     # Словарь для замены значений в шаблоне
#     replacements = {}

#      # Получаем значения из Streamlit input
#     kn_input_value = st.text_input("Введите Кадастровый", "")
#     replacements['<КадастровыйНомер>'] = kn_input_value

#     # Получаем значения из Streamlit input
#     fio_input_value = st.text_input("Введите ФИО п.1.3", "")
#     replacements['<ФИО>'] = fio_input_value

#     # Получаем значения из Streamlit input
#     num_request_input_value = st.text_input("Номер завявления", "")
#     replacements['<НомерЗаявления>'] = num_request_input_value
   
#     request_date_value = st.date_input("Дата поступления обращения","today",format='DD/MM/YYYY')
#     replacements['<ДатаПоступленияЗаявления>'] = str(request_date_value.strftime('%d.%m.%Y'))

#     email = st.text_input("Почта")
#     replacements['<Почта>'] = email

#     # Кнопка для замены данных в шаблоне
#     if st.button("Заменить данные в шаблоне"):
#         replace_text(doc, replacements)
#         st.success("Данные успешно заменены в шаблоне!")

#         # Сохраняем измененный файл
#         doc.save('output.docx')

# if __name__ == "__main__":
#     main()


