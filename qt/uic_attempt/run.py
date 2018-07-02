from PyQt5 import QtGui, QtWidgets, uic

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi('uis/mainwindow.ui', self)

if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())