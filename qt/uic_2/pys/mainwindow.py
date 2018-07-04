# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess

from arbitraria import Ui_Arbitraria
from constante1 import Ui_Constante1
from constante2 import Ui_Constante2
from estatica import Ui_Estatica
from resultados import Ui_Resultados

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("* { background-color: rgb(11, 173, 224) }\n"
"QPushButton { border-radius: 5px; background-color: white; border-bottom: 1px solid black }\n"
"QPushButton:hover { background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(238, 238, 238, 255)) }")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.titulo = QtWidgets.QLabel(self.centralWidget)
        self.titulo.setGeometry(QtCore.QRect(0, 40, 801, 111))
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
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 177, 801, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.menu_main = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.menu_main.setContentsMargins(200, 11, 200, 11)
        self.menu_main.setSpacing(6)
        self.menu_main.setObjectName("menu_main")
        self.button_arbitrario = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_arbitrario.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_arbitrario.sizePolicy().hasHeightForWidth())
        self.button_arbitrario.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.button_arbitrario.setFont(font)
        self.button_arbitrario.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_arbitrario.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_arbitrario.setFlat(True)
        self.button_arbitrario.setObjectName("button_arbitrario")

        self.button_arbitrario.clicked.connect(self.on_arbitraria_clicked)

        self.menu_main.addWidget(self.button_arbitrario)
        self.button_constante1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_constante1.sizePolicy().hasHeightForWidth())
        self.button_constante1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.button_constante1.setFont(font)
        self.button_constante1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_constante1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_constante1.setFlat(True)
        self.button_constante1.setObjectName("button_constante1")

        self.button_constante1.clicked.connect(self.on_constante1_clicked)

        self.menu_main.addWidget(self.button_constante1)
        self.button_constante2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_constante2.sizePolicy().hasHeightForWidth())
        self.button_constante2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.button_constante2.setFont(font)
        self.button_constante2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_constante2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_constante2.setFlat(True)
        self.button_constante2.setObjectName("button_constante2")

        self.button_constante2.clicked.connect(self.on_constante2_clicked)

        self.menu_main.addWidget(self.button_constante2)
        self.button_estatica = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_estatica.sizePolicy().hasHeightForWidth())
        self.button_estatica.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.button_estatica.setFont(font)
        self.button_estatica.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_estatica.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_estatica.setFlat(True)
        self.button_estatica.setObjectName("button_estatica")

        self.button_estatica.clicked.connect(self.on_estatica_clicked)

        self.menu_main.addWidget(self.button_estatica)
        spacerItem = QtWidgets.QSpacerItem(0, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.menu_main.addItem(spacerItem)
        self.button_info = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_info.sizePolicy().hasHeightForWidth())
        self.button_info.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.button_info.setFont(font)
        self.button_info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_info.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_info.setFlat(True)
        self.button_info.setObjectName("button_info")

        self.button_info.clicked.connect(self.on_info_clicked)

        self.menu_main.addWidget(self.button_info)
        self.button_exit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_exit.sizePolicy().hasHeightForWidth())
        self.button_exit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.button_exit.setFont(font)
        self.button_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_exit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_exit.setFlat(True)
        self.button_exit.setObjectName("button_exit")

        self.button_exit.clicked.connect(MainWindow.close)

        self.menu_main.addWidget(self.button_exit)
        self.versao = QtWidgets.QLabel(self.centralWidget)
        self.versao.setGeometry(QtCore.QRect(0, 540, 801, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versao.sizePolicy().hasHeightForWidth())
        self.versao.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.versao.setFont(font)
        self.versao.setStyleSheet("color: white")
        self.versao.setAlignment(QtCore.Qt.AlignCenter)
        self.versao.setObjectName("versao")
        #MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DIMduct"))
        self.titulo.setText(_translate("MainWindow", "DIMduct"))
        self.button_arbitrario.setText(_translate("MainWindow", "Arbitrária"))
        self.button_constante1.setText(_translate("MainWindow", "Constante"))
        self.button_constante2.setText(_translate("MainWindow", "Constante 2"))
        self.button_estatica.setText(_translate("MainWindow", "Estática"))
        self.button_info.setText(_translate("MainWindow", "Informações (PDF)"))
        self.button_exit.setText(_translate("MainWindow", "Sair"))
        self.versao.setText(_translate("MainWindow", "v. 11-17"))

    def on_arbitraria_clicked(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Arbitraria()
        self.ui.setupUi(self.window)

        self.window.show()

    def on_constante1_clicked(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Constante1()
        self.ui.setupUi(self.window)

        self.window.show()

    def on_constante2_clicked(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Constante2()
        self.ui.setupUi(self.window)

        self.window.show()

    def on_estatica_clicked(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Estatica()
        self.ui.setupUi(self.window)

        self.window.show()

    def on_info_clicked(self):
        subprocess.Popen(['manual.pdf'], shell=True)