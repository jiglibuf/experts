import pandas as pd

import pandas as pd

class ExcelHoarder:
    def __init__(self, replacements):
        self.replacements = replacements
        self.name = ''
        self.purpose = ''
        self.area = ''
        self.postive_floor = ''
        self.negative_floor = ''
        self.wall_type = ''
        self.foundation_year = ''
        self.kn_zu = ''
        self.type_p = ''
        
        # Read the Excel file
        try:
            self.data = pd.read_excel('данные\Расчеты\ЗП НЗ_ЗП ЖЗ_ЗП ОНС.xlsx', dtype= object ,decimal=',', header=0)
            self.template_path_data = pd.read_excel('данные\Способ определения.xlsx')
        except FileNotFoundError:
            print("File not found. Please check the file path.")
    def get_template_path(self):
        if 'Кадастровый номер' in self.template_path_data.columns:
            match = self.template_path_data.loc[self.template_path_data['Кадастровый номер'] == self.replacements.conditions['<КадастровыйНомер>'],['Модель оценки, использованная при определении КС']]
            model = match.iloc[0,0]
            if model in ['ЗП НЗ','ЗП ЖЗ', 'ЗП ГСК']:
                template_path = 'данные\Шаблоны РЗ\РЗ-НЗ_ЖЗ_ГСК.docx'
            elif model in ['ЗП ОНС']:
                template_path = 'данные\Шаблоны РЗ\Ответ РЗ-ОНС.docx'
            else:
                print('Нет шаблона')
            if not match.empty:
                self.replacements.update_conditions('<Модель определения>',model)
                self.replacements.update_template_path(template_path)
            else:
                print('Пусто в template_path_data по этому кн')
    # def tables_page1(self):

    #     # Check if 'Кадастровый номер' exists in the data columns
    #     if 'Кадастровый номер' in self.data.columns:
    #         # Find rows where 'Кадастровый номер' matches kn_input_value
    #         matches = self.data.loc[self.data['Кадастровый номер'] == self.replacements.conditions['<КадастровыйНомер>'], 
    #                                 ['Наименование здания', 'Назначение/Проектируемое назначение здания', 'Вид объекта недвижимости','Площадь ЕГРН в 1 лист','Адрес','Кол-во надземных этажей ЕГРН','Кол-во подземных этажей ЕГРН',
    #                                  'Материал стен ЕГРН','Год ввода в эксплуатацию ЕГРН','Площадь, иная характеристика в 5.3','Кадастровый номер земельного участка','кол-во надземных этажей в 5.3','Количество подземных этажей в 5.3',
    #                                  'Материал стен в 5.3','Год ввода в эксплуатацию в 5.3']]

    #         # Check if there are any matches
    #         if not matches.empty:
    #             # таблица 1
    #             building_name = matches.iloc[0, 0]  # First column
    #             purpose = matches.iloc[0, 1]  # Second column
    #             type_p = matches.iloc[0, 2]  # Third column
    #             area_egrn = str(matches.iloc[0, 3])  # Third column
    #             adress = matches.iloc[0, 4]  # Third column
    #             postive_floor = str(matches.iloc[0, 5])  # Third column
    #             negative_floor = str(matches.iloc[0, 6])  # Third column
    #             wall_type = matches.iloc[0, 7]  # Third column
    #             foundation_year = str(matches.iloc[0, 8])  # Third column
    #             kn_zu = matches.iloc[0, 10]
    #             if kn_zu == 'nan':
    #                 kn_zu = str(kn_zu)  # Third column
    #             else: kn_zu = '-'
    #             #таблица 2
    #             area2 = str(matches.iloc[0, 9])  # Third column
    #             postive_floor2 = str(matches.iloc[0, 11])  # Third column
    #             negative_floor2 = str(matches.iloc[0, 12])  # Third column
    #             wall_type2 = str(matches.iloc[0, 13])
    #             foundation_year2 = str(matches.iloc[0, 14])

    #             # Update the conditions
    #             # таблица 1
    #             self.replacements.update_conditions('<Наименование>', anchor=building_name)
    #             self.replacements.update_conditions('<Назначение>', anchor=purpose)
    #             self.replacements.update_conditions('<Вид_объекта>', anchor=type_p)
    #             self.replacements.update_conditions('<Площадь>', anchor=area_egrn)
    #             self.replacements.update_conditions('<Адрес>', anchor=adress)
    #             self.replacements.update_conditions('<Этажи+>', anchor=postive_floor)
    #             self.replacements.update_conditions('<Этажи->', anchor=negative_floor)
    #             self.replacements.update_conditions('<Материал_стен>', anchor=wall_type)
    #             self.replacements.update_conditions('<Год_ввода>', anchor=foundation_year)
    #             self.replacements.update_conditions('<КН_ЗУ>', anchor=kn_zu)

    #             #таблица 2
    #             self.replacements.update_conditions('<2Этажи+>', anchor=postive_floor2)
    #             self.replacements.update_conditions('<2Этажи->', anchor=negative_floor2)
    #             self.replacements.update_conditions('<2Материал_стен>', anchor=wall_type2)
    #             self.replacements.update_conditions('<2Год_ввода>', anchor=foundation_year2)
    #             self.replacements.update_conditions('<2Площадь>', anchor=area2)



    #         else:
    #             print(f"No building name found for 'Кадастровый номер': {self.replacements.conditions['<КадастровыйНомер>']}")
    #     else:
    #         print("'Кадастровый номер' column not found in the Excel data.")

    def tables_page1(self):
        # Check if 'Кадастровый номер' exists in the data columns
        if 'Кадастровый номер' in self.data.columns:
            # Find rows where 'Кадастровый номер' matches kn_input_value
            matches = self.data.loc[self.data['Кадастровый номер'] == self.replacements.conditions['<КадастровыйНомер>']]

            # Check if there are any matches
            if not matches.empty:
                for column_name in matches.columns:
                    # Проверяем, что значение не NaN и имя столбца не содержит "Unnamed"
                    if not column_name.startswith('Unnamed'):
                        # Получаем значение из таблицы и обновляем соответствующее условие
                        value = str(matches.iloc[0][column_name])
                        if value !='nan':
                            # Создаем ключ в нужном формате и обновляем условие
                            key = f"<{column_name}>"
                            value = self.process_percents_and_rounding(key,value)
                            self.replacements.update_conditions(key, anchor=value)

            else:
                print(f"No building name found for 'Кадастровый номер': {self.replacements.conditions['<КадастровыйНомер>']}")
        else:
            print("'Кадастровый номер' column not found in the Excel data.")
        try:
            self.replacements.conditions['<Кадастровый номер земельного участка>']
            
        except:
            self.replacements.update_conditions('<Кадастровый номер земельного участка>',anchor='-')

    def process_p_5(self):
        if self.replacements.conditions['<Справочник>'] =='УПВС':
            self.replacements.update_conditions('<воспроизводство/замещение>',anchor='воспроизводство')
        if self.replacements.conditions['<Справочник>'] =='КО-ИНВЕСТ':
            self.replacements.update_conditions('<воспроизводство/замещение>',anchor='замещение')
        else:
            pass
        try:
            self.replacements.conditions['<Объем в 5.3>']
        except:
            self.replacements.update_conditions('<Объем в 5.3>',anchor='-')

    def process_percents_and_rounding(self, key, value):
        if key in ['<Внешнее устаревание>','<Накопленный износ>']:
            return str(round(float(value)*100, 2))
        elif key in ['<УПКС 2023>','<Затраты на замещение / воспроизводство с учетом ПП и ДКЗ>']:
            return str(round(float(value), 2))
        else:
            return value
        # self.replacements.update_conditions('<воспроизводство/замещение>',anchor='воспроизводство')
        # self.replacements.update_conditions('<воспроизводство/замещение>',anchor='воспроизводство')

            
    def update_replacements(self):
        self.get_template_path()
        self.tables_page1()
        self.process_p_5()
