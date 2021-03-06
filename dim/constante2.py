# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'constante2.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import math
from scipy.optimize import fsolve

from dim.resultados import Ui_Resultados
from dim.erro import Ui_Erro

class Ui_Constante2(object):
    def setupUi(self, Constante2):
        Constante2.setObjectName("Constante2")
        Constante2.resize(800, 600)
        Constante2.setStyleSheet("QWidget { background-color: rgb(11, 173, 224) }\n"
"QPushButton { border-radius: 5px; background-color: white; border-bottom: 1px solid black }\n"
"QPushButton:hover { background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(238, 238, 238, 255)) }\n"
"QLineEdit, QComboBox { background-color: white; color: black }\n"
"QComboBox { border-radius: 2px; border: 1px solid lightgrey }\n"
"QComboBox::item { background-color: white }\n"
"QComboBox::item:selected { background-color: rgb(11, 173, 224) }\n"
"QLabel { color: white }\n"
"QCheckBox { height: 25px; margin-left: 83.5% }") #pq esse número? não sei, parece centralizado assim

        self.titulo = QtWidgets.QLabel(Constante2)
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
        self.pushButton = QtWidgets.QPushButton(Constante2)
        self.pushButton.setGeometry(QtCore.QRect(200, 510, 401, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.calcula)

        self.formLayoutWidget = QtWidgets.QWidget(Constante2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 160, 801, 326))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(200, 0, 200, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        self.lineEdit_7.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)

        self.check = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.check.setObjectName("check")
        self.check.toggle()
        self.check.toggled.connect( self.change_fields )
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.check)

        #self.lineEdit_8 = QtWidgets.QLineEdit(self.formLayoutWidget)
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        #self.lineEdit_8.setSizePolicy(sizePolicy)
        #self.lineEdit_8.setBaseSize(QtCore.QSize(0, 0))
        #font = QtGui.QFont()
        #font.setFamily("Roboto")
        #font.setPointSize(12)
        #self.lineEdit_8.setFont(font)
        #self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        #self.lineEdit_8.setObjectName("lineEdit_8")
        #self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)

        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_9.setFont(font)
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_9.setStatusTip("")
        self.label_9.setStyleSheet("text-decoration: underline; font-size: 16px")
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")

        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setStyleSheet("background-color: lightgray")

        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_10.setFont(font)
        self.label_10.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_10.setStatusTip("")
        self.label_10.setStyleSheet("text-decoration: underline; font-size: 16px")
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setObjectName("lineEdit_10")

        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setStyleSheet("background-color: lightgray")

        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)

        self.retranslateUi(Constante2)
        QtCore.QMetaObject.connectSlotsByName(Constante2)

    def retranslateUi(self, Constante2):
        _translate = QtCore.QCoreApplication.translate
        Constante2.setWindowTitle(_translate("Constante2", "DIMduct >> Constante (2)"))
        self.titulo.setText(_translate("Constante2", "DIMduct"))
        self.pushButton.setText(_translate("Constante2", "Calcular"))
        self.label.setText(_translate("Constante2", "Temperatura (°C):"))
        self.label_2.setText(_translate("Constante2", "Comprimento do Trecho (m):"))
        self.label_3.setText(_translate("Constante2", "Vazão do Trecho (m³/s):"))
        self.label_4.setText(_translate("Constante2", "Ângulo Total de Curvas (°):"))
        self.label_5.setText(_translate("Constante2", "Rugosidade Absoluta (m):"))
        self.label_6.setText(_translate("Constante2", "Vazão do Trecho Ant. (m³/s):"))
        self.label_7.setText(_translate("Constante2", "Velocidade Ant. (m/s):"))
        self.label_8.setText(_translate("Constante2", "Primeiro trecho?"))
        self.label_9.setToolTip(_translate("Constante2", "Será calculado no primeiro trecho."))
        self.label_9.setWhatsThis(_translate("Constante2", "Será calculado no primeiro trecho."))
        self.label_9.setText(_translate("Constante2", "Perda de Carga (Pa/m):"))
        self.label_10.setToolTip(_translate("Constante2", "Será calculado no primeiro trecho."))
        self.label_10.setWhatsThis(_translate("Constante2", "Será calculado no primeiro trecho."))
        self.label_10.setText(_translate("Constante2", "Diâmetro 2-3 (m):"))

    def change_fields(self):
        if self.check.isChecked():
            style = "background-color: lightgray"
            self.lineEdit_9.setReadOnly(True)
            self.lineEdit_10.setReadOnly(True)
            self.lineEdit_9.setStyleSheet(style)
            self.lineEdit_10.setStyleSheet(style)
        else:
            style = "background-color: white"
            self.lineEdit_9.setReadOnly(False)
            self.lineEdit_10.setReadOnly(False)
            self.lineEdit_9.setStyleSheet(style)
            self.lineEdit_10.setStyleSheet(style)

    def calcula(self):
        # calculos
        results = {}
        input_v = {}

        try:
            temp = float(self.lineEdit.text())
            input_v[self.label.text()] = str(temp)
            L_23 = float(self.lineEdit_2.text())
            input_v[self.label_2.text()] = str(L_23)
            Q_23 = float(self.lineEdit_3.text())
            input_v[self.label_3.text()] = str(Q_23)
            theta = float(self.lineEdit_4.text())
            input_v[self.label_4.text()] = str(theta)
            epsilon = float(self.lineEdit_5.text())
            input_v[self.label_5.text()] = str(epsilon)
            Q_1 = float(self.lineEdit_6.text())
            input_v[self.label_6.text()] = str(Q_1)
            u_1 = float(self.lineEdit_7.text())
            input_v[self.label_7.text()] = str(u_1)
            trecho1 = self.check.isChecked()
            input_v[self.label_8.text()] = "Sim" if trecho1 else "Não"

            rho = 101303 /(286.9 *(temp + 273.15))
            mu = ((13 + 0.1 * temp)* 0.000001)* rho
            if trecho1:
                D_1 = math.sqrt((4.0 * Q_1) / (math.pi * u_1)) 
                Re_i = rho * u_1 * D_1 / mu
                f_0_i = math.pow(-1.8 * math.log10(math.pow(epsilon / (3.7 * D_1), 1.11) + 6.9 / Re_i), -2.0)
                f_i = math.pow(-2.0 * math.log10(epsilon / (3.7 * D_1) + 2.51 / (Re_i * math.sqrt(f_0_i))), -2.0)
                dP_m1 = (f_i * L_23 / D_1 + 0.1 * theta / 90.0) * u_1 ** 2.0 * rho
                D_23_i = D_1
            else:
                dP_m1 = float(self.lineEdit_9.text())
                input_v[self.label_9.text()] = str(dP_m1)
                D_23_i = float(self.lineEdit_10.text())
                input_v[self.label_10.text()] = str(D_23_i)

            u_23_i = u_1

            def residuals(initial):
                D_23 = initial[0]
                u_23 = initial[1]
                residual = [0.0, 0.0]
                global Re
                global f
                Re = rho * u_23 * D_23 / mu
                f_0 = (-1.8 * math.log10(math.pow(epsilon / (3.7 * D_23), 1.11) + 6.9 / Re)) ** -2.0
                f = (-2.0 * math.log10(epsilon / (3.7 * D_23) + 2.51 / (Re * math.sqrt(f_0)))) ** -2.0
                residual[0] = (f * L_23 / D_23 + 0.1 * theta / 90.0)*u_23**2.0 - dP_m1    
                residual[1] = D_23 - math.sqrt((4.0 * Q_23) / (math.pi * u_23))
                return residual
        
            D_23, u_23 = fsolve(residuals, [D_23_i, u_23_i])

            def arredonda(val):
                return ("%.3f" % val)

            results["D2-3"] = arredonda(D_23) + " m"
            results["u2-3"] = arredonda(u_23) + " m/s"
            if trecho1 == 1 :
                results["D1"] = arredonda(D_1) + " m"
            results["dP m1"] = arredonda(dP_m1) + " Pa/m"

            # janela
            self.window = QtWidgets.QDialog()
            self.ui = Ui_Resultados()
            self.ui.setupUi(self.window, results, input_v)

            self.window.setWindowIcon(QtGui.QIcon('./imgs/icon.ico'))

            self.window.show()
            
        except Exception as e:
            self.erro = QtWidgets.QDialog()
            self.ui = Ui_Erro()

            if(isinstance(e, ValueError)):
                self.ui.setupUi(self.erro, "Algum campo inválido.\n")
            else:
                self.ui.setupUi(self.erro, "Algo deu errado:\n"+str(e))
    
            self.erro.setWindowIcon(QtGui.QIcon('./imgs/icon.ico'))

            self.erro.show()