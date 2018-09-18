# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'estatica.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import math
from scipy.optimize import fsolve

from dim.resultados import Ui_Resultados
from dim.erro import Ui_Erro

class Ui_Estatica(object):
    def setupUi(self, Estatica):
        Estatica.setObjectName("Estatica")
        Estatica.resize(800, 600)
        Estatica.setStyleSheet("QWidget { background-color: rgb(11, 173, 224) }\n"
"QPushButton { border-radius: 5px; background-color: white; border-bottom: 1px solid black }\n"
"QPushButton:hover { background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(238, 238, 238, 255)) }\n"
"QLabel{ color: white }\n"
"QLineEdit{ background-color: white; color: black }\n"
"QCheckBox { height: 25px; margin-left: 83.5% }")

        self.titulo = QtWidgets.QLabel(Estatica)
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
        self.pushButton = QtWidgets.QPushButton(Estatica)
        self.pushButton.setGeometry(QtCore.QRect(200, 520, 401, 51))
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

        self.formLayoutWidget = QtWidgets.QWidget(Estatica)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 170, 801, 326))
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
        self.lineEdit_8 = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.label_9.setFont(font)
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
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_10.setStatusTip("")
        self.label_10.setStyleSheet("text-decoration: underline; font-size: 16px")
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_10)

        self.check = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.check.setObjectName("check")
        self.check.toggle()
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.check)

        #self.lineEdit_10 = QtWidgets.QLineEdit(self.formLayoutWidget)
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        #self.lineEdit_10.setSizePolicy(sizePolicy)
        #self.lineEdit_10.setBaseSize(QtCore.QSize(0, 0))
        #font = QtGui.QFont()
        #font.setFamily("Roboto")
        #font.setPointSize(12)
        #self.lineEdit_10.setFont(font)
        #self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        #self.lineEdit_10.setObjectName("lineEdit_10")
        #self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)

        self.retranslateUi(Estatica)
        QtCore.QMetaObject.connectSlotsByName(Estatica)

    def retranslateUi(self, Estatica):
        _translate = QtCore.QCoreApplication.translate
        Estatica.setWindowTitle(_translate("Estatica", "DIMduct >> Estática"))
        self.titulo.setText(_translate("Estatica", "DIMduct"))
        self.pushButton.setText(_translate("Estatica", "Calcular"))
        self.label.setText(_translate("Estatica", "Temperatura (°C):"))
        self.label_2.setText(_translate("Estatica", "Comprimento do Trecho (m):"))
        self.label_3.setText(_translate("Estatica", "Vazão do Trecho (m³/s):"))
        self.label_4.setText(_translate("Estatica", "Velocidade Anterior (m/s):"))
        self.label_5.setText(_translate("Estatica", "Ângulo Total de Curvas (°):"))
        self.label_6.setText(_translate("Estatica", "Fator de Recuperação:"))
        self.label_7.setText(_translate("Estatica", "Rugosidade Absoluta (m):"))
        self.label_8.setText(_translate("Estatica", "Chute Diâmetro (m):"))
        self.label_9.setText(_translate("Estatica", "Chute Velocidade (m/s):"))
        self.label_10.setText(_translate("Estatica", "Calcular perda de carga?"))
        self.label_10.setToolTip(_translate("Estatica", "Ativar para o primeiro trecho e cálculo de curva."))
        self.label_10.setWhatsThis(_translate("Estatica", "Ativar para o primeiro trecho e cálculo de curva."))

    def calcula(self):
        # calculos
        results = {}
        input_v = {}

        try:
            temp = float(self.lineEdit.text())
            input_v[self.label.text()] = str(temp)
            L_23 = float(self.lineEdit_2.text()) # Comprimento do Trecho Atual
            input_v[self.label_2.text()] = str(L_23)
            Q_23 = float(self.lineEdit_3.text()) # Vazão do Trecho Atual
            input_v[self.label_3.text()] = str(Q_23)
            u_12 = float(self.lineEdit_4.text())
            input_v[self.label_4.text()] = str(u_12)
            theta = float(self.lineEdit_5.text())
            input_v[self.label_5.text()] = str(theta)
            R = float(self.lineEdit_6.text())
            input_v[self.label_6.text()] = str(R)
            epsilon = float(self.lineEdit_7.text()) #Rugosidade
            input_v[self.label_7.text()] = str(epsilon)
            D_23_i = float(self.lineEdit_8.text())
            input_v[self.label_8.text()] = str(D_23_i)
            u_23_i = float(self.lineEdit_9.text())
            input_v[self.label_9.text()] = str(u_23_i)
            trecho1 = float(self.check.isChecked())
            input_v[self.label_10.text()] = "Sim" if trecho1 else "Não"

            # valores fora desses limites (~) não funcionam.
            # desse jeito, não importa o que o usuário colocar, sempre vai dar certo
            if u_23_i < 2.7:
                u_23_i = 2.7
            elif u_23_i > 41: #41.787441101002
                u_23_i = 41

            if D_23_i <= 0:
                D_23_i = 0.1
            elif D_23_i > 6:
                D_23_i = 6

            rho = 101303 /(286.9 *(temp + 273.15))
            mu = ((13 + 0.1 * temp)* 0.000001)* rho

            def residuals(initial):
                D_23 = initial[0]
                u_23 = initial[1]
                residual = [0.0, 0.0]
                global Re
                global f
                Re = rho * u_23 * D_23 / mu
                f_0 = math.pow(-1.8 * math.log10(math.pow(epsilon / (3.7 * D_23), 1.11) + 6.9 / Re), -2.0)
                f = math.pow(-2.0 * math.log10(epsilon / (3.7 * D_23) + 2.51 / (Re * math.sqrt(f_0))), -2.0)
                residual[0] = (f * L_23 / D_23 + 0.1 * theta / 90.0 + R) * u_23 ** 2.0 - R * u_12 ** 2.0
                residual[1] = D_23 - math.sqrt((4.0 * Q_23) / (math.pi * u_23))
                return residual
               

            D_23, u_23 = fsolve(residuals, [D_23_i, u_23_i])
            if trecho1:
                dP = (rho*f*L_23*u_23**2.0/(D_23*2.0))
            A = (math.pi*D_23**2.0)/4.0

            def arredonda(val):
                return ("%.3f" % val)

            results["D2-3"] = arredonda(D_23) + " m" # 3 casas
            results["u2-3"] = arredonda(u_23) + " m/s" #2 casas
            results["A"] = arredonda(A) + " m²" # 3 casas
            results["f"] = arredonda(f) # 4 casas
            if trecho1:
                results["dP"] = arredonda(dP) + " Pa" # 3 casas

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
                self.ui.setupUi(self.erro, "Algum campo inválido.\n"+str(e))
            else:
                self.ui.setupUi(self.erro, "Algo deu errado:\n"+str(e))
    
            self.erro.setWindowIcon(QtGui.QIcon('./imgs/icon.ico'))

            self.erro.show()