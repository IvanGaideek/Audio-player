# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yt_des.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_YtForm(object):
    def setupUi(self, YtForm):
        YtForm.setObjectName("YtForm")
        YtForm.resize(500, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("For_Qtdesiner/icon_youtube.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        YtForm.setWindowIcon(icon)
        YtForm.setStyleSheet("QMainWindow, QWidget {\n"
"    background-color: qlineargradient(spread:pad, x1:0.300818, y1:0.312, x2:1, y2:1, stop:0.357955 rgba(0, 63, 162, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(YtForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(YtForm)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line_url = QtWidgets.QLineEdit(YtForm)
        self.line_url.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.line_url.setFont(font)
        self.line_url.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.line_url.setAcceptDrops(True)
        self.line_url.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.line_url.setStyleSheet("border: 1px solid #edeef0;\n"
"padding-left: 4px;\n"
"border-radius: 4px;\n"
"padding-top: 5px;\n"
"padding-bottom: 5px;\n"
"background-color: rgba(255, 255, 255, 0.1);\n"
"\n"
"\n"
"")
        self.line_url.setText("")
        self.line_url.setMaxLength(100)
        self.line_url.setFrame(True)
        self.line_url.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_url.setCursorPosition(0)
        self.line_url.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.line_url.setDragEnabled(False)
        self.line_url.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.line_url.setClearButtonEnabled(False)
        self.line_url.setObjectName("line_url")
        self.horizontalLayout.addWidget(self.line_url)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(YtForm)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.line_title = QtWidgets.QLineEdit(YtForm)
        self.line_title.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.line_title.setFont(font)
        self.line_title.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.line_title.setAcceptDrops(True)
        self.line_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.line_title.setStyleSheet("border: 1px solid #edeef0;\n"
"padding-left: 4px;\n"
"border-radius: 4px;\n"
"background-color: rgb(38, 133, 162);")
        self.line_title.setText("")
        self.line_title.setMaxLength(100)
        self.line_title.setFrame(True)
        self.line_title.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_title.setCursorPosition(0)
        self.line_title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.line_title.setDragEnabled(False)
        self.line_title.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.line_title.setClearButtonEnabled(False)
        self.line_title.setObjectName("line_title")
        self.verticalLayout_2.addWidget(self.line_title)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(YtForm)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);\n"
"margin: 35px 0;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.line_save = QtWidgets.QLineEdit(YtForm)
        self.line_save.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.line_save.setFont(font)
        self.line_save.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.line_save.setAcceptDrops(True)
        self.line_save.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.line_save.setStyleSheet("border: 1px solid #edeef0;\n"
"padding-left: 4px;\n"
"border-radius: 4px;\n"
"padding-top: 5px;\n"
"padding-bottom: 5px;\n"
"background-color: rgba(255, 255, 255, 0.1);")
        self.line_save.setText("")
        self.line_save.setMaxLength(100)
        self.line_save.setFrame(True)
        self.line_save.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_save.setCursorPosition(0)
        self.line_save.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.line_save.setDragEnabled(False)
        self.line_save.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.line_save.setClearButtonEnabled(False)
        self.line_save.setObjectName("line_save")
        self.horizontalLayout_2.addWidget(self.line_save)
        self.btn_select = QtWidgets.QPushButton(YtForm)
        self.btn_select.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_select.setFont(font)
        self.btn_select.setStyleSheet("QPushButton {\n"
"    background-color: rgba(43, 236, 236, 0.3);\n"
"    border-radius:4px;\n"
"    border-color: rgb(235, 235, 235);\n"
"    color: #ffffff;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 55, 238);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 55, 238, 0.5);\n"
"}")
        self.btn_select.setIconSize(QtCore.QSize(128, 128))
        self.btn_select.setFlat(False)
        self.btn_select.setObjectName("btn_select")
        self.horizontalLayout_2.addWidget(self.btn_select)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_download = QtWidgets.QPushButton(YtForm)
        self.btn_download.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btn_download.setFont(font)
        self.btn_download.setStyleSheet("QPushButton {\n"
"    background-color: rgb(11, 255, 31);\n"
"    border-radius:4px;\n"
"    border-color: #ff0000;\n"
"    color: rgb(62, 38, 200);\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 55, 238);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 55, 238, 0.5);\n"
"}")
        self.btn_download.setIconSize(QtCore.QSize(128, 128))
        self.btn_download.setFlat(False)
        self.btn_download.setObjectName("btn_download")
        self.horizontalLayout_3.addWidget(self.btn_download)
        self.progressBar = QtWidgets.QProgressBar(YtForm)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 3)
        self.verticalLayout_2.setStretch(3, 2)
        self.verticalLayout_2.setStretch(4, 3)
        self.verticalLayout_2.setStretch(5, 3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.label = QtWidgets.QLabel(YtForm)
        self.label.setStyleSheet("border: 1px solid #edeef0;\n"
"padding-left: 4px;\n"
"border-radius: 4px;\n"
"padding-top: 5px;\n"
"padding-bottom: 5px;\n"
"background-color: rgba(255, 255, 255, 0.1);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(YtForm)
        QtCore.QMetaObject.connectSlotsByName(YtForm)

    def retranslateUi(self, YtForm):
        _translate = QtCore.QCoreApplication.translate
        YtForm.setWindowTitle(_translate("YtForm", "You Tube Music"))
        self.label_3.setText(_translate("YtForm", "Ссылка на видео"))
        self.line_url.setPlaceholderText(_translate("YtForm", " https://www.youtube.com/watch"))
        self.label_2.setText(_translate("YtForm", "Как вы хотите назвать скаченный файл(необязательно):"))
        self.line_title.setPlaceholderText(_translate("YtForm", "Используйте символы которыми можно называть файлы"))
        self.label_4.setText(_translate("YtForm", "Сохранить в"))
        self.line_save.setPlaceholderText(_translate("YtForm", " Укажите каталог для сохранения"))
        self.btn_select.setText(_translate("YtForm", "Выбрать"))
        self.btn_download.setText(_translate("YtForm", "Скачать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    YtForm = QtWidgets.QWidget()
    ui = Ui_YtForm()
    ui.setupUi(YtForm)
    YtForm.show()
    sys.exit(app.exec_())
