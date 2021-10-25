# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assistant/gui/base.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(897, 481)
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        self.central_widget_v_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.central_widget_v_layout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_v_layout.setObjectName("central_widget_v_layout")
        self.main_frame = QtWidgets.QFrame(self.central_widget)
        self.main_frame.setStyleSheet("QFrame {\n"
"    background-color: rgb(35, 39, 49);\n"
"    border-radius: 10px;\n"
"}")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.main_v_layout = QtWidgets.QVBoxLayout(self.main_frame)
        self.main_v_layout.setContentsMargins(0, 0, 0, 0)
        self.main_v_layout.setObjectName("main_v_layout")
        self.title_frame = QtWidgets.QFrame(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_frame.sizePolicy().hasHeightForWidth())
        self.title_frame.setSizePolicy(sizePolicy)
        self.title_frame.setMinimumSize(QtCore.QSize(0, 40))
        self.title_frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.title_frame.setToolTipDuration(-1)
        self.title_frame.setStyleSheet("QFrame {\n"
"}")
        self.title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_frame.setObjectName("title_frame")
        self.title_h_layout = QtWidgets.QHBoxLayout(self.title_frame)
        self.title_h_layout.setContentsMargins(0, 0, 10, 0)
        self.title_h_layout.setObjectName("title_h_layout")
        self.min_button = QtWidgets.QPushButton(self.title_frame)
        self.min_button.setMinimumSize(QtCore.QSize(20, 20))
        self.min_button.setMaximumSize(QtCore.QSize(20, 20))
        self.min_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(67, 203, 68);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(67, 220, 68);\n"
"}")
        self.min_button.setText("")
        self.min_button.setObjectName("min_button")
        self.title_h_layout.addWidget(self.min_button)
        self.max_button = QtWidgets.QPushButton(self.title_frame)
        self.max_button.setMinimumSize(QtCore.QSize(20, 20))
        self.max_button.setMaximumSize(QtCore.QSize(20, 20))
        self.max_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(248, 188, 58);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(255, 200, 58);\n"
"}")
        self.max_button.setText("")
        self.max_button.setObjectName("max_button")
        self.title_h_layout.addWidget(self.max_button)
        self.exit_button = QtWidgets.QPushButton(self.title_frame)
        self.exit_button.setMinimumSize(QtCore.QSize(20, 20))
        self.exit_button.setMaximumSize(QtCore.QSize(20, 20))
        self.exit_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(243, 91, 90);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: rgb(255, 91, 90);\n"
"}")
        self.exit_button.setText("")
        self.exit_button.setObjectName("exit_button")
        self.title_h_layout.addWidget(self.exit_button)
        self.main_v_layout.addWidget(self.title_frame)
        self.content_frame = QtWidgets.QFrame(self.main_frame)
        self.content_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_frame.setObjectName("content_frame")
        self.content_v_layout = QtWidgets.QVBoxLayout(self.content_frame)
        self.content_v_layout.setContentsMargins(-1, -1, -1, 0)
        self.content_v_layout.setObjectName("content_v_layout")
        self.widget_frame = QtWidgets.QFrame(self.content_frame)
        self.widget_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.widget_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.widget_frame.setObjectName("widget_frame")
        self.widget_v_layout = QtWidgets.QVBoxLayout(self.widget_frame)
        self.widget_v_layout.setObjectName("widget_v_layout")
        self.label = QtWidgets.QLabel(self.widget_frame)
        self.label.setStyleSheet("QLabel{\n"
        "    color: #e3e3e3;\n"
        "    font-size: 10vh;\n"
        "}")
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.widget_v_layout.addWidget(self.label)
        self.content_v_layout.addWidget(self.widget_frame)
        self.input_frame = QtWidgets.QFrame(self.content_frame)
        self.input_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.input_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.input_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_frame.setObjectName("input_frame")
        self.input_h_layout = QtWidgets.QHBoxLayout(self.input_frame)
        self.input_h_layout.setContentsMargins(0, 0, 0, 6)
        self.input_h_layout.setObjectName("input_h_layout")
        self.input_box = QtWidgets.QLineEdit(self.input_frame)
        self.input_box.setMinimumSize(QtCore.QSize(0, 40))
        self.input_box.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.input_box.setFont(font)
        self.input_box.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(35, 39, 49);\n"
"    color: rgb(236, 236, 236);\n"
"    border: 1px solid rgb(236, 236, 236);\n"
"    border-radius: 7px;\n"
"}")
        self.input_box.setText("")
        self.input_box.setFrame(True)
        self.input_box.setCursorPosition(0)
        self.input_box.setDragEnabled(True)
        self.input_box.setClearButtonEnabled(True)
        self.input_box.setObjectName("input_box")
        self.input_h_layout.addWidget(self.input_box)
        self.enter_button = QtWidgets.QPushButton(self.input_frame)
        self.enter_button.setMinimumSize(QtCore.QSize(40, 40))
        self.enter_button.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(20)
        font.setBold(True)
        #font.setWeight(75)
        self.enter_button.setFont(font)
        self.enter_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(242, 80, 34);\n"
"    color: rgb(235, 235, 235);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: rgb(255, 80, 34);\n"
"}")
        self.enter_button.setObjectName("enter_button")
        self.input_h_layout.addWidget(self.enter_button)
        self.content_v_layout.addWidget(self.input_frame)
        self.main_v_layout.addWidget(self.content_frame)
        self.central_widget_v_layout.addWidget(self.main_frame)
        main_window.setCentralWidget(self.central_widget)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "MainWindow"))
        self.input_box.setPlaceholderText(_translate("main_window", " Enter text here"))
        self.enter_button.setText(_translate("main_window", ">"))
