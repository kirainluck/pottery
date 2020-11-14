from PyQt5 import QtWidgets
from pottery import Ui_MainWindow  # imported ui
import sys


class AppMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(AppMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])
application = AppMainWindow()
application.show()

sys.exit(app.exec())