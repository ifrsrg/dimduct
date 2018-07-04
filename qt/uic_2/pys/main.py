from PyQt5.QtWidgets import QApplication, QDialog
from mainwindow import Ui_MainWindow

import sys

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_MainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())