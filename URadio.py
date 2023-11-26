import csv

from radio_ui import Ui_Form
from PyQt5.QtWidgets import QWidget


class ChangeRadio(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # загрузка интерфейса
        self.setGeometry(470, 250, 450, 520)
        self.setFixedSize(420, 220)
        self.add_flow.clicked.connect(self.add)
        self.del_flow.clicked.connect(self.delete)

    def add(self):
        self.result.setText('')
        list_file = []
        if len(self.title_radio.text().strip()) != 0:
            try:
                with open('radio_url.csv', 'r', newline='', encoding='utf-8') as file:
                    reader = csv.reader(file, delimiter=';', quotechar="'")
                    for i in reader:
                        list_file.append(i)
            except FileNotFoundError:
                pass
            finally:
                with open('radio_url.csv', 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file, delimiter=';', quotechar="'")
                    writer.writerow(['название радио', 'url адрес'])
                    for i in list_file[1:]:
                        writer.writerow(i)
                    if self.title_radio.text().strip() not in [j[0] for j in list_file]:
                        writer.writerow([self.title_radio.text().strip(), self.url_radio.text().strip()])
                        self.result.setText('Радио успешно добавлено')
                    else:
                        self.result.setText('Такое название радио уже существует!')
        else:
            self.result.setText('Не введено название радио!')

    def delete(self):
        self.result.setText('')
        element_to_delete = self.title_radio.text().strip()
        rows = []
        try:
            with open('radio_url.csv', 'r', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=';', quotechar="'")
                for row in reader:
                    rows.append(row)
        except FileNotFoundError:
            self.result.setText('Файла не существует, но я его создал')
        updated_rows = []
        for row in list(rows[1:]):
            if row[0] != element_to_delete:
                updated_rows.append(row)
            else:
                self.result.setText('Радио успешно удалено')
        updated_rows.append(['название радио', 'url адрес'])
        with open('radio_url.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, quotechar="'", delimiter=';')
            writer.writerows(updated_rows[::-1])

    @staticmethod  # для того чтобы получить метод без инициализации класса
    def radio_return():
        try:
            with open('radio_url.csv', 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=';', quotechar="'")
                return list(list(reader)[1:])
        except FileNotFoundError:
            return []

