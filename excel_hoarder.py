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
        self.type = ''

        # Read the Excel file
        try:
            self.data = pd.read_excel('данные\Расчеты\ЗП НЗ_ЗП ЖЗ_ЗП ОНС.xlsx', dtype={'Кадастровый номер': str})
        except FileNotFoundError:
            print("File not found. Please check the file path.")

    def find_name(self):

        # Check if 'Кадастровый номер' exists in the data columns
        if 'Кадастровый номер' in self.data.columns:
            # Find rows where 'Кадастровый номер' matches kn_input_value
            matches = self.data.loc[self.data['Кадастровый номер'] == self.replacements.conditions['<КадастровыйНомер>'], 
                                    ['Наименование здания', 'Назначение/Проектируемое назначение здания', 'Вид объекта недвижимости','Площадь ЕГРН в 1 лист']]

            # Check if there are any matches
            if not matches.empty:
                building_name = matches.iloc[0, 0]  # First column
                purpose = matches.iloc[0, 1]  # Second column
                type = matches.iloc[0, 2]  # Third column
                area = str(matches.iloc[0, 3])  # Third column

                # Update the conditions
                self.replacements.update_conditions('<Наименование>', anchor=building_name)
                self.replacements.update_conditions('<Назначение>', anchor=purpose)
                self.replacements.update_conditions('<Вид_объекта>', anchor=type)
                self.replacements.update_conditions('<Площадь>', anchor=area)
            else:
                print(f"No building name found for 'Кадастровый номер': {self.replacements.conditions['<КадастровыйНомер>']}")
        else:
            print("'Кадастровый номер' column not found in the Excel data.")

    def update_replacements(self):
        self.find_name()
