# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultados.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Resultados(object):
    def setupUi(self, Resultados, results, input_v={"--":"--"}):

        self.results = results
        self.input_v = input_v

        Resultados.setObjectName("Resultados")
        Resultados.resize(800, 600)
        Resultados.setStyleSheet("QWidget { background-color: rgb(11, 173, 224) }\n"
"QPushButton { border-radius: 5px; background-color: white; border-bottom: 1px solid black }\n"
"QPushButton:hover { background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(238, 238, 238, 255)) }\n"
"QLabel{ color: white }\n"
"QLineEdit{ background-color: white; color: black }")

        self.widget = Resultados #pra poder acessar lá no export

        self.okButton = QtWidgets.QPushButton(Resultados)
        self.okButton.setGeometry(QtCore.QRect(200, 410, 401, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okButton.sizePolicy().hasHeightForWidth())
        self.okButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.okButton.setFont(font)
        self.okButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.okButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.okButton.setFlat(True)
        self.okButton.setObjectName("okButton")

        self.okButton.clicked.connect(Resultados.close)

        self.exportButton = QtWidgets.QPushButton(Resultados)
        self.exportButton.setGeometry(QtCore.QRect(200, 480, 401, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exportButton.sizePolicy().hasHeightForWidth())
        self.exportButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.exportButton.setFont(font)
        self.exportButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exportButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.exportButton.setFlat(True)
        self.exportButton.setObjectName("exportButton")

        self.exportButton.clicked.connect(self.export)

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
	        self.labelsleft[label_index].setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
	        self.formLayout.setWidget(label_index, QtWidgets.QFormLayout.LabelRole, self.labelsleft[label_index])
	        self.labelsleft[label_index].setText(_translate("Resultados", key))

	        self.labelsright.append( QtWidgets.QLabel(self.formLayoutWidget) )
	        font = QtGui.QFont()
	        font.setFamily("Roboto")
	        font.setPointSize(12)
	        self.labelsright[label_index].setFont(font)
	        self.labelsright[label_index].setAlignment(QtCore.Qt.AlignCenter)
	        self.labelsright[label_index].setObjectName("labelr_"+str(label_index))
	        self.labelsright[label_index].setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
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
        self.okButton.setText(_translate("Resultados", "OK"))
        self.exportButton.setText(_translate("Resultados", "Exportar"))
        self.titulo.setText(_translate("Resultados", "DIMduct"))

    def export(self):

        import subprocess
        import os
        from datetime import datetime

        self.fileselect_window = QtWidgets.QFileDialog()

        exp_file, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget ,"Salvando Resultados","","Text Files (*.txt);;All Files (*)")
        if exp_file:

            file = open(exp_file, 'w')

            file.write("Entrada:\n")

            for key in self.input_v:
        
                file.write('  ' + key + ' ' + str(self.input_v[key]) + '\n')

            file.write('\n')
            file.write('Resultados:\n')

            for key in self.results:

                file.write('  ' + key + ': ' + str(self.results[key]) + '\n')