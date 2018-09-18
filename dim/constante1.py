# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'constante1.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import math

from dim.resultados import Ui_Resultados
from dim.erro import Ui_Erro

class Ui_Constante1(object):
    def setupUi(self, Constante1):
        Constante1.setObjectName("Constante1")
        Constante1.resize(800, 600)
        Constante1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Constante1.setStyleSheet("QWidget { background-color: rgb(11, 173, 224) }\n"
"QPushButton { border-radius: 5px; background-color: white; border-bottom: 1px solid black }\n"
"QPushButton:hover { background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(238, 238, 238, 255)) }\n"
"QLineEdit, QComboBox { background-color: white; color: black }\n"
"QComboBox { border-radius: 2px; border: 1px solid lightgrey }\n"
"QComboBox QAbstractItemView { background-color: white }\n"
"QComboBox:!editable, QComboBox::drop-down:editable { color: black }\n"
"QLabel { color: white }")

        self.formLayoutWidget = QtWidgets.QWidget(Constante1)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 170, 801, 261))
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

        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_7.setStatusTip("")
        self.label_7.setStyleSheet("text-decoration: underline; font-size: 16px")

        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.titulo = QtWidgets.QLabel(Constante1)
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
        self.pushButton = QtWidgets.QPushButton(Constante1)
        self.pushButton.setGeometry(QtCore.QRect(200, 450, 401, 51))
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

        self.retranslateUi(Constante1)
        QtCore.QMetaObject.connectSlotsByName(Constante1)

    def retranslateUi(self, Constante1):
        _translate = QtCore.QCoreApplication.translate
        Constante1.setWindowTitle(_translate("Constante1", "DIMduct >> Constante (1)"))
        self.label.setText(_translate("Constante1", "Temperatura (°C):"))
        self.label_2.setText(_translate("Constante1", "Comprimento do Trecho (m):"))
        self.label_3.setText(_translate("Constante1", "Vazão do Trecho 1 (m³/s):"))
        self.label_4.setText(_translate("Constante1", "Vazão do Trecho 2 (m³/s):"))
        self.label_5.setText(_translate("Constante1", "Ângulo Total de Curvas (°):"))
        self.label_6.setText(_translate("Constante1", "Rugosidade Absoluta (m):"))
        self.label_7.setText(_translate("Constante1", "Tipo:"))
        self.label_7.setToolTip(_translate("Constante1", "Pode ser que a seleção pareça estar em branco.\nPara resolver, clique em algum campo."))
        self.label_7.setWhatsThis(_translate("Constante1", "Pode ser que a seleção pareça estar em branco.\nPara resolver, clique em algum campo."))
        self.comboBox.setItemText(0, _translate("Constante1", "Conforto"))
        self.comboBox.setItemText(1, _translate("Constante1", "Industrial"))
        self.titulo.setText(_translate("Constante1", "DIMduct"))
        self.pushButton.setText(_translate("Constante1", "Calcular"))

    def calcula(self):
        # calculos
        results = {}
        input_v = {}

        try:
            temp = float(self.lineEdit.text())
            input_v[self.label.text()] = str(temp)
            L_1 = float(self.lineEdit_2.text())
            input_v[self.label_2.text()] = str(L_1)
            Q_1 = float(self.lineEdit_3.text())
            input_v[self.label_3.text()] = str(Q_1)
            Q_2 = float(self.lineEdit_4.text())
            input_v[self.label_4.text()] = str(Q_2)
            theta = float(self.lineEdit_5.text())
            input_v[self.label_5.text()] = str(theta)
            epsilon = float(self.lineEdit_6.text())
            input_v[self.label_6.text()] = str(epsilon)
            tipo = self.comboBox.currentIndex()
            input_v[self.label_7.text()] = str(self.comboBox.currentText())

            rho = 101303 /(286.9 *(temp + 273.15))
            mu = ((13 + 0.1 * temp)* 0.000001)* rho

            const_tipo = 25 if tipo else 32 #tipo==0 -> 32, tipo==1 -> 25

            Q_1L = Q_1*1000.0 #[l/s]
            D_1 = const_tipo*(math.pow(Q_1L, 0.38))/1000
            A_1 = (math.pi*D_1**2.0)/4.0
            u_1 = Q_1/A_1
            
            Q_2L = Q_2*1000.0 #[l/s]
            D_2 = const_tipo*(math.pow(Q_2L, 0.38))/1000
            A_2 = (math.pi*D_2**2.0)/4.0
            u_2 = Q_2/A_2

               
            Re = rho * u_1 * D_1 / mu
            f_0 = math.pow(-1.8 * math.log10(math.pow(epsilon / (3.7 * D_1), 1.11) + 6.9 / Re), -2.0)
            f = math.pow(-2.0 * math.log10(epsilon / (3.7 * D_1) + 2.51 / (Re * math.sqrt(f_0))), -2.0)
            dP_m = (f * L_1 / D_1 + 0.1 * theta / 90.0) * u_1 ** 2.0 * rho

            def arredonda(val):
                return ("%.3f" % val)
           
            results["D1"] = arredonda(D_1) + " m"
            results["u1"] = arredonda(u_1) + " m/s"
            results["A1"] = arredonda(A_1) + " m²"
            results["D2"] = arredonda(D_2) + " m"
            results["u2"] = arredonda(u_2) + " m/s" 
            results["A2"] = arredonda(A_2) + " m²"
            results["dP m"] = arredonda(dP_m) + " Pa/m"

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

        