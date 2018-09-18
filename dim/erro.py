# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'erro.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Erro(object):
    def setupUi(self, Form, msg):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        Form.setStyleSheet("* { background-color: rgb(11, 173, 224) }\n"
"QPushButton { border-radius: 5px; background-color: white; border-bottom: 1px solid black }\n"
"QPushButton:hover { background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(238, 238, 238, 255)) }")

        self.titulo = QtWidgets.QLabel(Form)
        self.titulo.setGeometry(QtCore.QRect(0, 40, 641, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titulo.sizePolicy().hasHeightForWidth())
        self.titulo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(85)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("color: white")
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 380, 401, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(Form.close)

        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 179, 641, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: white")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)

        self.retranslateUi(Form, msg)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form, msg):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Erro"))
        self.titulo.setText(_translate("Form", "DIMduct"))
        self.pushButton.setText(_translate("Form", "OK"))
        self.label_11.setText(_translate("Form", msg))

