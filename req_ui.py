# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'req.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(624, 846)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dataEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.dataEdit.setGeometry(QtCore.QRect(20, 100, 181, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dataEdit.setFont(font)
        self.dataEdit.setText("")
        self.dataEdit.setObjectName("dataEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 76, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.fabulaInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.fabulaInput.setGeometry(QtCore.QRect(20, 160, 581, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.fabulaInput.setFont(font)
        self.fabulaInput.setLineWidth(0)
        self.fabulaInput.setObjectName("fabulaInput")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 136, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 336, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.personInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.personInput.setEnabled(True)
        self.personInput.setGeometry(QtCore.QRect(20, 530, 581, 191))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.personInput.setFont(font)
        self.personInput.setReadOnly(True)
        self.personInput.setPlainText("")
        self.personInput.setObjectName("personInput")
        self.readyButton = QtWidgets.QPushButton(self.centralwidget)
        self.readyButton.setGeometry(QtCore.QRect(20, 780, 581, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.readyButton.setFont(font)
        self.readyButton.setObjectName("readyButton")
        self.numberEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.numberEdit.setGeometry(QtCore.QRect(210, 100, 211, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.numberEdit.setFont(font)
        self.numberEdit.setText("")
        self.numberEdit.setObjectName("numberEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 79, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.mpRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.mpRadioButton.setGeometry(QtCore.QRect(20, 10, 231, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mpRadioButton.setFont(font)
        self.mpRadioButton.setAcceptDrops(False)
        self.mpRadioButton.setToolTipDuration(-1)
        self.mpRadioButton.setAutoFillBackground(False)
        self.mpRadioButton.setChecked(True)
        self.mpRadioButton.setObjectName("mpRadioButton")
        self.udRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.udRadioButton.setGeometry(QtCore.QRect(20, 40, 181, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.udRadioButton.setFont(font)
        self.udRadioButton.setObjectName("udRadioButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 76, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.placeEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.placeEdit.setGeometry(QtCore.QRect(430, 100, 171, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.placeEdit.setFont(font)
        self.placeEdit.setObjectName("placeEdit")
        self.bornEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.bornEdit.setGeometry(QtCore.QRect(450, 360, 151, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bornEdit.setFont(font)
        self.bornEdit.setReadOnly(False)
        self.bornEdit.setDate(QtCore.QDate(2000, 1, 1))
        self.bornEdit.setObjectName("bornEdit")
        self.fioEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.fioEdit.setGeometry(QtCore.QRect(20, 360, 411, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fioEdit.setFont(font)
        self.fioEdit.setObjectName("fioEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(450, 339, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 387, 67, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.adressTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.adressTextEdit.setGeometry(QtCore.QRect(20, 410, 581, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adressTextEdit.sizePolicy().hasHeightForWidth())
        self.adressTextEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.adressTextEdit.setFont(font)
        self.adressTextEdit.setObjectName("adressTextEdit")
        self.addPersonButton = QtWidgets.QPushButton(self.centralwidget)
        self.addPersonButton.setGeometry(QtCore.QRect(480, 480, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addPersonButton.setFont(font)
        self.addPersonButton.setObjectName("addPersonButton")
        self.redCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.redCheckBox.setGeometry(QtCore.QRect(20, 730, 181, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.redCheckBox.setFont(font)
        self.redCheckBox.setObjectName("redCheckBox")
        self.delPersonButton = QtWidgets.QPushButton(self.centralwidget)
        self.delPersonButton.setGeometry(QtCore.QRect(480, 730, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.delPersonButton.setFont(font)
        self.delPersonButton.setObjectName("delPersonButton")
        self.clearPersonButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearPersonButton.setGeometry(QtCore.QRect(340, 730, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.clearPersonButton.setFont(font)
        self.clearPersonButton.setObjectName("clearPersonButton")
        self.defaultButton = QtWidgets.QPushButton(self.centralwidget)
        self.defaultButton.setGeometry(QtCore.QRect(430, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.defaultButton.setFont(font)
        self.defaultButton.setObjectName("defaultButton")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 500, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 624, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ReqQt"))
        self.label.setText(_translate("MainWindow", "Дата:"))
        self.label_2.setText(_translate("MainWindow", "Фабула:"))
        self.label_3.setText(_translate("MainWindow", "ФИО лица:"))
        self.readyButton.setText(_translate("MainWindow", "Готово"))
        self.label_4.setText(_translate("MainWindow", "Номер уд/мп:"))
        self.mpRadioButton.setText(_translate("MainWindow", "Материал проверки"))
        self.udRadioButton.setText(_translate("MainWindow", "Уголовное дело"))
        self.label_5.setText(_translate("MainWindow", "Населенный пункт:"))
        self.bornEdit.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.label_7.setText(_translate("MainWindow", "Дата рождения:"))
        self.label_8.setText(_translate("MainWindow", "Адрес:"))
        self.adressTextEdit.setPlainText(_translate("MainWindow", "Республика Коми, Сыктывдинский район,"))
        self.addPersonButton.setText(_translate("MainWindow", "Добавить"))
        self.redCheckBox.setText(_translate("MainWindow", "Редактировать"))
        self.delPersonButton.setText(_translate("MainWindow", "Удалить"))
        self.clearPersonButton.setText(_translate("MainWindow", "Очистить"))
        self.defaultButton.setText(_translate("MainWindow", "По умолчанию"))
        self.label_9.setText(_translate("MainWindow", "Список лиц:"))

