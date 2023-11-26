from inf_ui import Ui_Form
from PyQt5.QtWidgets import QWidget


class Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # загрузка интерфейса
        self.setGeometry(490, 250, 450, 520)
        with open('inf.txt', 'r', encoding='utf-8') as file:
            self.textBrowser.append(file.read())
