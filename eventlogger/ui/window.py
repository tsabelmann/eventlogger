# Import C
import csv

# Import D
import datetime

# Import E
from eventlogger.ui import UI_PATH

# Import P
import pathlib

# Import P
from PySide2 import QtCore, QtWidgets
from PySide2.QtUiTools import QUiLoader

# Import S
import sys

# Paths
WINDOW_PATH = UI_PATH.joinpath(pathlib.Path("window.ui")).resolve()


class MainWindow(QtCore.QObject):
    def __init__(self):
        super().__init__()

        # Loader
        loader = QUiLoader()
        self.ui = loader.load(str(WINDOW_PATH), None)

        # Data
        self.data = dict()

        # Label DateTime
        self.on_update_datetime()

        # Timer
        self.timer = QtCore.QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.on_update_datetime)
        self.timer.start()

        # Actions
        self.ui.actionSave.triggered.connect(self.on_save)
        self.ui.actionClear.triggered.connect(self.on_clear)
        self.ui.actionQuit.triggered.connect(self.on_quit)
        self.ui.actionAddTextAndClear.triggered.connect(self.on_add_text_and_clear)
        self.ui.actionAddTextAndKeep.triggered.connect(self.on_add_text_and_keep)

        # Signal
        self.ui.pushButton.clicked.connect(self.on_add_button_clicked)

        # Show UI
        self.ui.show()

    # Actions
    def on_save(self):
        with open(f"{datetime.datetime.now()}.csv", "w+") as fp:
            writer = csv.writer(fp, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([u"DateTime", "Text"])

            for dt, text in self.data.items():
                writer.writerow([dt.strftime("%D %H:%M:%S"), text])

    def on_clear(self):
        self.data.clear()

    def on_quit(self):
        sys.exit(0)

    def append_data(self):
        dt = datetime.datetime.now()
        text = self.ui.textField.toPlainText()
        self.data[dt] = text

    def on_add_text_and_clear(self):
        # Append data to data
        self.append_data()

        # Clear
        self.ui.textField.setText(u"")

    def on_add_text_and_keep(self):
        # Append data to data
        self.append_data()

    # Signals
    def on_add_button_clicked(self):
        self.on_add_text_and_clear()

    def on_update_datetime(self):
        dt = datetime.datetime.now()
        self.ui.label.setText(dt.strftime("%D %H:%M:%S"))