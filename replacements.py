class Replacements:
    def __init__(self):
        self.kn_input_value = ''
        self.kc_input_value = ''
        self.kc_selected_value = ''
        self.fio_input_value = ''
        self.num_request_input_value = ''
        self.request_date_value = ''
        self.email = ''
        self.docname = ''
        self.template_path = ''
        self.conditions = {}  # Словарь для условий

    def update(self, key, value=None, anchor=None):
        if value is None and anchor is None:
            return
        if anchor is not None:
            self.conditions[key] = anchor
        else:
            self.conditions[key] = value

    def as_dict(self):
        return {
            '<КадастровыйНомер>': self.kn_input_value,
            '<КадастроваяСтоимость>': self.kc_input_value,
            '<АкутальнаяКС>': self.kc_selected_value,
            '<ФИО>': self.fio_input_value,
            '<НомерЗаявления>': self.num_request_input_value,
            '<ДатаПоступленияЗаявления>': self.request_date_value,
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