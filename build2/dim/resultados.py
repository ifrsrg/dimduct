# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultados.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Resultados(object):
    def setupUi(self, Resultados, results):
        Resultados.setObjectName("Resultados")
        Resultados.resize(800, 600)
        Resultados.setStyleSheet("QWidget { background-color: rgb(11, 173, 224) }\n"
"QPushButton { border-radius: 5px; background-color: white; border-bottom: 1px solid black }\n"
"QPushButton:hover { background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(238, 238, 238, 255)) }\n"
"QLabel{ color: white }\n"
"QLineEdit{ background-color: white; color: black }")

        self.pushButton = QtWidgets.QPushButton(Resultados)
        self.pushButton.setGeometry(QtCore.QRect(200, 410, 401, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(Resultados.close)

        self.formLayoutWidget = QtWidgets.QWidget(Resultados)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 160, 801, 206))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(200, 0, 200, 0)
        self.formLayout.setObjectName("formLayout")

        self.labelsleft = []
        self.labelsright = []

        _translate = QtCore.QCoreApplication.translate

        for key in results:

        	label_index = len(self.labelsleft)

	        self.labelsleft.append( QtWidgets.QLabel(self.formLayoutWidget) )
	        font = QtGui.QFont()
	        font.setFamily("Roboto")
	        font.setPointSize(12)
	        self.labelsleft[label_index].setFont(font)
	        self.labelsleft[label_index].setObjectName("labell_"+str(label_index))
	        self.formLayout.setWidget(label_index, QtWidgets.QFormLayout.LabelRole, self.labelsleft[label_index])
	        self.labelsleft[label_index].setText(_translate("Resultados", key))

	        self.labelsright.append( QtWidgets.QLabel(self.formLayoutWidget) )
	        font = QtGui.QFont()
	        font.setFamily("Roboto")
	        font.setPointSize(12)
	        self.labelsright[label_index].setFont(font)
	        self.labelsright[label_index].setAlignment(QtCore.Qt.AlignCenter)
	        self.labelsright[label_index].setObjectName("labelr_"+str(label_index))
	        self.formLayout.setWidget(label_index, QtWidgets.QFormLayout.FieldRole, self.labelsright[label_index])
	        self.labelsright[label_index].setText(_translate("Resultados", results[key]))

        self.titulo = QtWidgets.QLabel(Resultados)
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

        self.retranslateUi(Resultados)
        QtCore.QMetaObject.connectSlotsByName(Resultados)

    def retranslateUi(self, Resultados):
        _translate = QtCore.QCoreApplication.translate
        Resultados.setWindowTitle(_translate("Resultados", "DIMduct >> Resultados"))
        self.pushButton.setText(_translate("Resultados", "OK"))
        self.titulo.setText(_translate("Resultados", "DIMduct"))

