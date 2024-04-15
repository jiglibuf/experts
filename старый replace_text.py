

def replace_text(doc, replacements):
    # Заменяем текст в колонтитулах
    for section in doc.sections:
        if section.header is not None:
            for paragraph in section.header.paragraphs:
                for key, value in replacements.items():
                    if key in paragraph.text:
                        new_text = paragraph.text.replace(key, value)
                        for run in paragraph.runs:
                            run.clear()
                        new_run = paragraph.add_run(new_text)
                        apply_text_style(new_run, paragraph.runs[0].font)

        if section.footer is not None:
            for paragraph in section.footer.paragraphs:
                for key, value in replacements.items():
                    if key in paragraph.text:
                        new_text = paragraph.text.replace(key, value)
                        for run in paragraph.runs:
                            run.clear()
                        new_run = paragraph.add_run(new_text)
                        apply_text_style(new_run, paragraph.runs[0].font)

    # Заменяем текст в основном тексте документа
    for paragraph in doc.paragraphs:
        for key, value in replacements.items():
            if key in paragraph.text:
                new_text = paragraph.text.replace(key, value)
                for run in paragraph.runs:
                    run.clear()
                new_run = paragraph.add_run(new_text)
                apply_text_style(new_run, paragraph.runs[0].font)

    # Заменяем текст в якорях таблиц
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    for key, value in replacements.items():
                        if key in paragraph.text:
                            new_text = paragraph.text.replace(key, value)
                            for run in paragraph.runs:
                                run.clear()
                            new_run = paragraph.add_run(new_text)
                            apply_text_style(new_run, paragraph.runs[0].font)

    # Удаление пустых строк
    for paragraph in doc.paragraphs:
        if paragraph.text.strip() == '':
            paragraph.clear()