from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtGui
from dim.mainwindow import Ui_MainWindow

import sys

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_MainWindow()
ui.setupUi(window)

window.setWindowIcon(QtGui.QIcon('./imgs/icon.ico'))

window.show()
sys.exit(app.exec_())