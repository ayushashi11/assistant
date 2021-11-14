import os
from .gui.window import run
from .ai_m2 import reply
from PySide6 import QtWidgets as qtw, QtCore as qtc
from pynput.keyboard import Listener, KeyCode, Key
from markdown import markdown as md

LOCK = False

def setup_reply_function(input_box: qtw.QLineEdit, label: qtw.QLabel):
    label.setTextFormat(qtc.Qt.RichText)
    def reply_function():
        text = input_box.text()
        input_box.setText("")
        res = reply(text)
        if type(res) == tuple:
            os.system("curl -L -o test.jpg "+res[1])
            label.setText('<img src="file:///home/prabhakar/assistant/test.jpg" style="width:20px;"/><br/>'+md(res[0]).replace('\n',"<br/>"))
            return
        label.setText(md(res).replace('\n',"<br/>"))
    return reply_function

def on_release_listen(key):
    global LOCK
    if key==Key.esc:
        return False
    key = str(key)
    print(repr(key))
    if key=="'\\x05'" and not LOCK:
        LOCK = True
        run(setup_reply_function)
        LOCK = False
    elif key=="'\\x03'":
        return False

with Listener(on_release=on_release_listen) as listener:
    listener.join()
