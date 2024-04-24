from replacements import Replacements

class DataProcessor:
     
    def __init__(self, replacements:Replacements):
        self.replacements = replacements
        self.osnovanie = None
    
    # def get_replacements_dict(self):
    #     return self.replacements_dict

    def process_p_3(self):  
        if self.replacements.conditions['<КадастроваяСтоимостьОбращения>'] == '':
                self.replacements.update_conditions('<Условие3_1>')
                self.replacements.update_conditions('<Условие3_2>', anchor ='')
                self.replacements.update_conditions('<Условие3_3>', anchor ='')
        else:
            if self.replacements.conditions['<АкутальнаяКС>'] == self.replacements.conditions['<КадастроваяСтоимостьОбращения>']:
                self.replacements.update_conditions('<Условие3_2>')
                self.replacements.update_conditions('<Условие3_1>', anchor ='')
                self.replacements.update_conditions('<Условие3_3>', anchor ='')

            else:
                self.replacements.update_conditions('<Условие3_3>')
                self.replacements.update_conditions('<Условие3_2>', anchor ='')
                self.replacements.update_conditions('<Условие3_1>', anchor ='')


    def process_p_4(self):
        if self.osnovanie =='ГКО':
            self.replacements.update_conditions('<Условие4.3_1>')
            self.replacements.update_conditions('<Условие4.3_2>', anchor ='')
            self.replacements.update_conditions('<Условие4.3_3>', anchor ='')
            self.replacements.update_conditions('<Условие4.3_4>', anchor ='')
            self.replacements.update_conditions('<Условие4.4>', anchor='Приказ Министерства имущественных и земельных отношений Камчатского края от 27.11.2023 № 42-Н «Об утверждении результатов определения кадастровой стоимости объектов недвижимости на территории Камчатского края»')
            self.replacements.update_conditions('<Условие4.2>', anchor='01.01.2023')
            self.replacements.update_conditions('<Условие4.5>', anchor='''Фонд данных государственной кадастровой оценки: 
https://rosreestr.gov.ru/wps/portal/p/cc_ib_portal_services/cc_ib_ais_fdgko
                                                
Официальный сайт бюджетного учреждения (порядок получения сведений о кадастровой стоимости):
https://gko.kamgov.ru/ocenka2023.php''')
            
        if self.replacements.docname in ['(в соответствии ст.16 Федерального закона от 03.07.2016 N 237-ФЗ «О государственной кадастровой оценке»)']:
            self.replacements.update_conditions('<Условие4.3_2>')
            self.replacements.update_conditions('<Условие4.3_1>', anchor ='')
            self.replacements.update_conditions('<Условие4.3_3>', anchor ='')
            self.replacements.update_conditions('<Условие4.3_4>', anchor ='')

        if self.replacements.docname in ['(в соответствии ст.15 Федерального закона от 03.07.2016 N 237-ФЗ «О государственной кадастровой оценке»)']:
            self.replacements.update_conditions('<Условие4.3_3>')
            self.replacements.update_conditions('<Условие4.3_2>', anchor ='')
            self.replacements.update_conditions('<Условие4.3_3>', anchor ='')
            self.replacements.update_conditions('<Условие4.3_4>', anchor ='')

        if self.replacements.docname in ['О внесении изменений в приказ Министерства имущественных и земельных отношений Камчатского края от 12.11.2020 N 179 «Об утверждении результатов определения кадастровой стоимости объектов капитального строительства, земельных участков категорий земель населенных пунктов, земель промышленности, энергетики, транспорта, связи, радиовещания, телевидения, информатики, земель для обеспечения космической деятельности, земель обороны, безопасности и земель иного специального назначения, расположенных на территории Камчатского края»',
                    'О внесении изменений в приказ Министерства имущественных и земельных отношений Камчатского края от 26.10.2022 N П-39 «Об утверждении результатов определения кадастровой стоимости земельных участков на территории Камчатского края»',
                    'О внесении изменений в приказ Министерства имущественных и земельных отношений Камчатского края от 27.11.2023 N 42-Н «Об утверждении результатов определения кадастровой стоимости объектов недвижимости на территории Камчатского края»'
                    ]:
            self.replacements.update_conditions('<Условие4.3_4>')
            self.replacements.update_conditions('<Условие4.3_1>', anchor ='')
            self.replacements.update_conditions('<Условие4.3_2>', anchor ='')
            self.replacements.update_conditions('<Условие4.3_3>', anchor ='')

        if not self.replacements.docname:
            # тут нужно вывести сообщение об ошибке
            pass
    
    def process_p_2(self):
        if self.replacements.kc_selected_value == self.replacements.kc_input_value:
            self.replacements.update_conditions('<Условие2_1>')
            self.replacements.update_conditions('<Условие2_2>', anchor='')

        else:
            self.replacements.update_conditions('<Условие2_2>')
            self.replacements.update_conditions('<Условие2_1>', anchor='')
    
    def get_osnovanie(self):
        if self.replacements.docname in ['Об утверждении результатов определения кадастровой стоимости зданий, помещений, сооружений, объектов незавершенного строительства, машино-мест на территории Камчатского края',
                    'Об утверждении результатов определения кадастровой стоимости объектов капитального строительства, земельных участков категорий земель населенных пунктов, земель промышленности, энергетики, транспорта, связи, радиовещания, телевидения, информатики, земель для обеспечения космической деятельности, земель обороны, безопасности и земель иного специального назначения, расположенных на территории Камчатского края',
                    'Об утверждении результатов определения кадастровой стоимости земельных участков категории земель сельскохозяйственного назначения, расположенных на территории Камчатского края',
                    'Об утверждении результатов определения кадастровой стоимости земельных участков на территории Камчатского края',
                    'Об утверждении результатов определения кадастровой стоимости зданий, помещений, сооружений, объектов незавершенного строительства, машино-мест на территории Камчатского края'
                    ]:
            self.osnovanie = 'ГКО'
            
        if self.replacements.docname in ['(в соответствии ст.16 Федерального закона от 03.07.2016 N 237-ФЗ «О государственной кадастровой оценке»)']:
            self.osnovanie = 'ст.16'
            
        if self.replacements.docname in ['(в соответствии ст.15 Федерального закона от 03.07.2016 N 237-ФЗ «О государственной кадастровой оценке»)']:
            self.osnovanie = 'ст.15'

        if self.replacements.docname in ['О внесении изменений в приказ Министерства имущественных и земельных отношений Камчатского края от 12.11.2020 N 179 «Об утверждении результатов определения кадастровой стоимости объектов капитального строительства, земельных участков категорий земель населенных пунктов, земель промышленности, энергетики, транспорта, связи, радиовещания, телевидения, информатики, земель для обеспечения космической деятельности, земель обороны, безопасности и земель иного специального назначения, расположенных на территории Камчатского края»',
                    'О внесении изменений в приказ Министерства имущественных и земельных отношений Камчатского края от 26.10.2022 N П-39 «Об утверждении результатов определения кадастровой стоимости земельных участков на территории Камчатского края»',
                    'О внесении изменений в приказ Министерства имущественных и земельных отношений Камчатского края от 27.11.2023 N 42-Н «Об утверждении результатов определения кадастровой стоимости объектов недвижимости на территории Камчатского края»'
                    ]:
            self.osnovanie = 'исправление ошибок'

        if not self.replacements.docname:
            # тут нужно вывести сообщение об ошибке
            pass
    
    def update_replacements(self):
        self.get_osnovanie()
        self.process_p_2()
        self.process_p_3()
        self.process_p_4()