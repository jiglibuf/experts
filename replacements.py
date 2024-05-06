


class Replacements:
    def __init__(self):
        self.kn_input_value = ''
        self.kc_input_value = ''
        self.kc_selected_value = ''
        self.fio_input_value = ''
        self.num_request_value = ''
        self.num_incoming_input_value = ''
        self.request_date_value = ''
        self.email = ''
        self.docname = ''
        self.template_path = ''
        self.fio_representative_input_value = ''
        self.request_adress = ''

        self.conditions = {}  # Словарь для условий

    def update(self, key, value=None, anchor=None):
        if value is None and anchor is None:
            return
        if anchor is not None:
            self.conditions[key] = anchor
        else:
            self.conditions[key] = value

    def update_attributes(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        return {
            '<КадастровыйНомер>': self.kn_input_value,
            '<КадастроваяСтоимостьОбращения>': self.kc_input_value,
            '<АкутальнаяКС>': self.kc_selected_value,
            '<ФИО>': self.fio_input_value,
            '<НомерЗаявления>': self.num_request_value,
            '<НомерВходящего>': self.num_incoming_input_value,
            '<ДатаПоступленияЗаявления>': self.request_date_value,
            '<Представитель>': self.fio_representative_input_value,
            '<АдресЗаявителя>': self.request_adress,
            '<Почта>': self.email,
            '<template_path>': self.template_path,
            **self.conditions  # Добавляем условия в словарь
        }
    def update_conditions(self, condition_to_update, anchor=None):
        if anchor is None:
            anchor = 'V'

        # Добавляем ключ, если его нет
        if condition_to_update not in self.conditions:
            self.conditions[condition_to_update] = anchor
        else:
            # Если ключ уже есть, обновляем значение
            self.conditions[condition_to_update] = anchor
            
    def update_docname(self, docname):
        self.docname = docname

    def update_email(self, email):
        self.email = email

    def update_template_path(self, template_path):
        self.template_path = template_path

    def replace_decimal_points(self):
        for key, value in self.conditions.items():
            if value.isdigit() and len(value) > 1 and value[0] == '0':
                    # Если значение состоит из цифр и начинается с нуля, оставляем его без изменений
                    pass
            elif isinstance(value, str) and '.' in value and value.count('.') == 1 and value[-1] != '.':
            # if isinstance(value, str) and '.' in value and value.count('.') == 1 and not self.is_date(value):
                # Если значение является строкой, содержит одну точку и не является датой, заменяем точку на запятую
                self.conditions[key] = value.replace('.', ',')
            
    
