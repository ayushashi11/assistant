from PySide2 import QtWidgets as qtw
from PySide2 import QtCore as qtc
from PySide2 import QtGui as qtg

from .base import Ui_main_window

from qtpy import uic
import sys


# For reference:
# class Window:
#     def __init__(self) -> None:
#         self.window = uic.loadUi("D:/Programming/Python/assistant/assistant/gui/base.ui")
#
#         self.exit_button = self.window
#
#         self.window.setWindowFlag(qtc.Qt.FramelessWindowHint)
#         self.window.setAttribute(qtc.Qt.WA_TranslucentBackground)
#
#         self.window.show()
#
#     def add_functionality(self) -> None:
#         ...
#         # self.window.


class Window(qtw.QMainWindow):
    def __init__(self) -> None:
        super().__init__(parent=None)
        main = Ui_main_window()
        main.setupUi(self)
        main.retranslateUi(self)


def setup() -> None:
    app = qtw.QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
