import sys

from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
from PySide6 import QtWidgets as qtw

from .base import Ui_main_window
from typing import Callable

class TitleFrame(qtw.QFrame):
    def __init__(self, window: qtw.QMainWindow) -> None:
        super().__init__(parent=window)
        self.window = window

        self.old_pos = self.window.pos()

    def mousePressEvent(self, event: qtg.QMouseEvent) -> None:
        self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event: qtg.QMouseEvent) -> None:
        delta = qtc.QPoint(event.globalPos() - self.old_pos)
        self.window.move(self.window.x() + delta.x(), self.window.y() + delta.y())
        self.old_pos = event.globalPos()


class Window(qtw.QMainWindow):
    def __init__(self) -> None:
        super().__init__(parent=None)
        self.window = Ui_main_window()
        self.window.setupUi(self)
        self.window.retranslateUi(self)

        self.setWindowFlag(qtc.Qt.FramelessWindowHint)
        self.setAttribute(qtc.Qt.WA_TranslucentBackground)

        self.size_grip: qtw.QSizeGrip = qtw.QSizeGrip(self)
        self.size_grip.setFixedWidth(10)

        self.dummy_title_frame: qtw.QFrame = TitleFrame(self)

        self.is_maximum: bool = False

        self.add_functionality()
        self.add_widget()
        self.window.enter_button.clicked.connect(lambda: print("clicked"))

    def add_widget(self) -> None:
        self.window.title_h_layout.insertWidget(0, self.size_grip)
        self.window.title_h_layout.insertWidget(1, self.dummy_title_frame)

    def add_functionality(self) -> None:
        self.window.exit_button.clicked.connect(self.exit_app)
        self.window.min_button.clicked.connect(self.minimise_app)
        self.window.max_button.clicked.connect(self.maximise_app)

    def exit_app(self) -> None:
        self.hide()
        sys.exit()

    def minimise_app(self) -> None:
        self.setWindowState(qtc.Qt.WindowMinimized)

    def maximise_app(self) -> None:
        if not self.is_maximum:
            self.setWindowState(qtc.Qt.WindowMaximized)
        else:
            self.setWindowState(qtc.Qt.WindowNoState)
        self.is_maximum = not self.is_maximum


def setup(fn: Callable[[qtw.QLineEdit, qtw.QLabel], Callable[[], None]]) -> None:
    app = qtw.QApplication(sys.argv)

    window = Window()
    window.window.enter_button.clicked.connect(fn(window.window.input_box, window.window.label))
    window.show()

    sys.exit(app.exec_())
