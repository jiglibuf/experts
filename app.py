from docx import Document
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
    

    # Создаем экземпляр класса DataInput
    data_input = DataInput(required_fields)

    # Получаем значения из Streamlit input
    data_input.get_input_values()
    data_input.show_actual_kc()
    data_input.get_selected_kc()
    # Получаем словарь для замены значений в шаблоне
    data_input.get_replacements_dict()

    
    # Кнопка для замены данных в шаблоне
    if st.button("Заменить данные в шаблоне"):
        
        # if not replacements['<КадастроваяСтоимость>']:
        #     replacements = update_conditions(replacements, 'Условие3_1')
        # else:
        #     if replacements['<АкутальнаяКС>'] == replacements['<КадастроваяСтоимость>']:
        #         st.write('равны')
        #         st.write(replacements['<АкутальнаяКС>'], replacements['<КадастроваяСтоимость>'])
        #         replacements = update_conditions(replacements, 'Условие3_2')
        #     else:
        #         st.write('не равны')
        #         st.write(replacements['<АкутальнаяКС>'], replacements['<КадастроваяСтоимость>'])
        #         replacements = update_conditions(replacements, 'Условие3_3')
        # p_4_3(docname,replacements)
        data_input.get_osnovanie()
        data_input.get_p_2()
        data_input.get_p_3()
        data_input.get_p_4()
        replace_text(doc, data_input.replacements)

        st.success("Данные успешно заменены в шаблоне!")
        # Сохраняем измененный файл
        doc.save('output.docx')

    # Закрываем соединение с базой данных

if __name__ == "__main__":
    main()
