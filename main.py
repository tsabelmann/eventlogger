# Import E
from eventlogger.ui.window import MainWindow

# Import P
from PySide2 import QtWidgets

# Import S
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    app.exec_()
