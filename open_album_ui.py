# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'open_album_des.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class OUi_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(558, 424)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("For_Qtdesiner/album_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget {\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(124, 8, 0);\n"
"    background-color: rgba(252, 255, 76, 0);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #edeef0;\n"
"    padding-left: 4px;\n"
"    border-radius: 4px;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgba(43, 236, 236, 0.3);\n"
"    border-radius:4px;\n"
"    border-color: rgb(235, 235, 235);\n"
"    color: rgb(84, 88, 147);\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(108, 198, 12);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(108, 198, 12, 0.5);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.title_album = QtWidgets.QLineEdit(Form)
        self.title_album.setObjectName("title_album")
        self.horizontalLayout.addWidget(self.title_album)
        self.delete_2 = QtWidgets.QPushButton(Form)
        self.delete_2.setStyleSheet("#delete_2:hover {\n"
"    background-color: rgb(255, 149, 0);\n"
"}\n"
"\n"
"#delete_2:pressed {\n"
"    background-color: rgba(255, 149, 0, 0.5);\n"
"}")
        self.delete_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("For_Qtdesiner/delete_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_2.setIcon(icon1)
        self.delete_2.setIconSize(QtCore.QSize(25, 25))
        self.delete_2.setObjectName("delete_2")
        self.horizontalLayout.addWidget(self.delete_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.check_song = QtWidgets.QCheckBox(Form)
        self.check_song.setStyleSheet("background-color: rgba(132, 116, 255, 0);\n"
"")
        self.check_song.setObjectName("check_song")
        self.verticalLayout.addWidget(self.check_song)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setStyleSheet("background-color:rgb(202, 98, 197);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.title_music = QtWidgets.QLineEdit(Form)
        self.title_music.setObjectName("title_music")
        self.horizontalLayout_2.addWidget(self.title_music)
        self.add_music = QtWidgets.QPushButton(Form)
        self.add_music.setObjectName("add_music")
        self.horizontalLayout_2.addWidget(self.add_music)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.way_file = QtWidgets.QLineEdit(Form)
        self.way_file.setWhatsThis("")
        self.way_file.setObjectName("way_file")
        self.horizontalLayout_4.addWidget(self.way_file)
        self.open_file = QtWidgets.QPushButton(Form)
        self.open_file.setObjectName("open_file")
        self.horizontalLayout_4.addWidget(self.open_file)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.create_album = QtWidgets.QPushButton(Form)
        self.create_album.setObjectName("create_album")
        self.verticalLayout.addWidget(self.create_album)
        self.result = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.result.setFont(font)
        self.result.setText("")
        self.result.setObjectName("result")
        self.verticalLayout.addWidget(self.result)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 4)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Создание нового альбома"))
        self.label.setText(_translate("Form", "Название альбома:"))
        self.check_song.setText(_translate("Form", "Удалить трек из альбома? Для этого не забудьте ввести название его и выбрать плейлист."))
        self.label_2.setText(_translate("Form", "Название трека(необязательно):"))
        self.add_music.setText(_translate("Form", "Добавить"))
        self.way_file.setToolTip(_translate("Form", "rjt"))
        self.way_file.setPlaceholderText(_translate("Form", "Путь к файлу"))
        self.open_file.setText(_translate("Form", "Выбрать"))
        self.create_album.setText(_translate("Form", "Создать альбом"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = OUi_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
