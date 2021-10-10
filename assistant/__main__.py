from .gui.window import setup
from .ai_m2 import reply
from PySide2 import QtWidgets as qtw, QtCore as qtc
from markdown import markdown as md

def setup_reply_function(input_box: qtw.QLineEdit, label: qtw.QLabel):
    label.setTextFormat(qtc.Qt.RichText)
    def reply_function():
        text = input_box.text()
        input_box.setText("")
        res = reply(text)
        print(repr(res))
        label.setText(md(res).replace('\n',"<br/>"))
    return reply_function

if __name__ == '__main__':
    setup(setup_reply_function)
