# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Work_Space\work_test\Python\Numpad\KeyBoard.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_KeyBoard(object):
    def setupUi(self, KeyBoard):
        KeyBoard.setObjectName("KeyBoard")
        KeyBoard.resize(382, 259)
        KeyBoard.setMaximumSize(QtCore.QSize(1000, 1000))
        KeyBoard.setAutoFillBackground(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(KeyBoard)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(KeyBoard)
        self.widget.setMaximumSize(QtCore.QSize(10000, 10000))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.widget.setFont(font)
        self.widget.setStyleSheet("QPushButton{\n"
"font: 75 12pt ;\n"
"}\n"
"QPushButton#btn_Show{text-align: left;}")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.btn_Show = QtWidgets.QPushButton(self.widget)
        self.btn_Show.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_Show.setMaximumSize(QtCore.QSize(198, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_Show.setFont(font)
        self.btn_Show.setText("")
        self.btn_Show.setAutoDefault(False)
        self.btn_Show.setDefault(False)
        self.btn_Show.setFlat(True)
        self.btn_Show.setObjectName("btn_Show")
        self.horizontalLayout.addWidget(self.btn_Show)
        self.btn_Hide = QtWidgets.QPushButton(self.widget)
        self.btn_Hide.setMinimumSize(QtCore.QSize(70, 45))
        self.btn_Hide.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_Hide.setFont(font)
        self.btn_Hide.setObjectName("btn_Hide")
        self.horizontalLayout.addWidget(self.btn_Hide)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_Again = QtWidgets.QPushButton(self.widget)
        self.btn_Again.setMinimumSize(QtCore.QSize(70, 45))
        self.btn_Again.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_Again.setFont(font)
        self.btn_Again.setObjectName("btn_Again")
        self.gridLayout.addWidget(self.btn_Again, 1, 4, 1, 1)
        self.btn_Del = QtWidgets.QPushButton(self.widget)
        self.btn_Del.setMinimumSize(QtCore.QSize(70, 45))
        self.btn_Del.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_Del.setFont(font)
        self.btn_Del.setObjectName("btn_Del")
        self.gridLayout.addWidget(self.btn_Del, 0, 4, 1, 1)
        self.btn_Cap = QtWidgets.QPushButton(self.widget)
        self.btn_Cap.setMinimumSize(QtCore.QSize(70, 45))
        self.btn_Cap.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_Cap.setFont(font)
        self.btn_Cap.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_Cap.setStyleSheet("")
        self.btn_Cap.setAutoRepeat(False)
        self.btn_Cap.setAutoExclusive(False)
        self.btn_Cap.setAutoDefault(False)
        self.btn_Cap.setDefault(False)
        self.btn_Cap.setFlat(False)
        self.btn_Cap.setObjectName("btn_Cap")
        self.buttonGroup = QtWidgets.QButtonGroup(KeyBoard)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.btn_Cap)
        self.gridLayout.addWidget(self.btn_Cap, 1, 0, 1, 1)
        self.btn_Num = QtWidgets.QPushButton(self.widget)
        self.btn_Num.setMinimumSize(QtCore.QSize(70, 45))
        self.btn_Num.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_Num.setFont(font)
        self.btn_Num.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_Num.setStyleSheet("")
        self.btn_Num.setAutoRepeat(False)
        self.btn_Num.setAutoExclusive(False)
        self.btn_Num.setAutoDefault(False)
        self.btn_Num.setDefault(False)
        self.btn_Num.setFlat(False)
        self.btn_Num.setObjectName("btn_Num")
        self.buttonGroup.addButton(self.btn_Num)
        self.gridLayout.addWidget(self.btn_Num, 0, 0, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.widget)
        self.btn_1.setMinimumSize(QtCore.QSize(70, 45))
        self.btn_1.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_1.setFont(font)
        self.btn_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_1.setStyleSheet("")
        self.btn_1.setAutoRepeat(False)
        self.btn_1.setAutoExclusive(False)
        self.btn_1.setAutoDefault(False)
        self.btn_1.setDefault(False)
        self.btn_1.setFlat(False)
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 0, 1, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.widget)
        self.btn_2.setMinimumSize(QtCore.QSize(70, 45))
        self.btn_2.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 0, 2, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.widget)
        self.btn_3.setMinimumSize(QtCore.QSize(70, 45))
        self.btn_3.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 0, 3, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.widget)
        self.btn_4.setMinimumSize(QtCore.QSize(70, 45))
        self.btn_4.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_4.setFont(font)
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 1, 1, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.widget)
        self.btn_5.setMinimumSize(QtCore.QSize(70, 45))
        self.btn_5.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_5.setFont(font)
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 1, 2, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.widget)
        self.btn_6.setMinimumSize(QtCore.QSize(70, 45))
        self.btn_6.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_6.setFont(font)
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 1, 3, 1, 1)
        self.btn_Sma = QtWidgets.QPushButton(self.widget)
        self.btn_Sma.setMinimumSize(QtCore.QSize(70, 45))
        self.btn_Sma.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_Sma.setFont(font)
        self.btn_Sma.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_Sma.setStyleSheet("")
        self.btn_Sma.setAutoRepeat(False)
        self.btn_Sma.setAutoExclusive(False)
        self.btn_Sma.setAutoDefault(False)
        self.btn_Sma.setDefault(False)
        self.btn_Sma.setFlat(False)
        self.btn_Sma.setObjectName("btn_Sma")
        self.buttonGroup.addButton(self.btn_Sma)
        self.gridLayout.addWidget(self.btn_Sma, 2, 0, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.widget)
        self.btn_7.setMinimumSize(QtCore.QSize(70, 45))
        self.btn_7.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_7.setFont(font)
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 2, 1, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.widget)
        self.btn_9.setMinimumSize(QtCore.QSize(70, 45))
        self.btn_9.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_9.setFont(font)
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 2, 3, 1, 1)
        self.btn_Wrap = QtWidgets.QPushButton(self.widget)
        self.btn_Wrap.setMinimumSize(QtCore.QSize(70, 45))
        self.btn_Wrap.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_Wrap.setFont(font)
        self.btn_Wrap.setCheckable(False)
        self.btn_Wrap.setObjectName("btn_Wrap")
        self.gridLayout.addWidget(self.btn_Wrap, 2, 4, 1, 1)
        self.btn_Sym = QtWidgets.QPushButton(self.widget)
        self.btn_Sym.setMinimumSize(QtCore.QSize(70, 45))
        self.btn_Sym.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_Sym.setFont(font)
        self.btn_Sym.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_Sym.setStyleSheet("")
        self.btn_Sym.setAutoRepeat(False)
        self.btn_Sym.setAutoExclusive(False)
        self.btn_Sym.setAutoDefault(False)
        self.btn_Sym.setDefault(False)
        self.btn_Sym.setFlat(False)
        self.btn_Sym.setObjectName("btn_Sym")
        self.buttonGroup.addButton(self.btn_Sym)
        self.gridLayout.addWidget(self.btn_Sym, 3, 0, 1, 1)
        self.btn_Space = QtWidgets.QPushButton(self.widget)
        self.btn_Space.setMinimumSize(QtCore.QSize(70, 45))
        self.btn_Space.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_Space.setFont(font)
        self.btn_Space.setObjectName("btn_Space")
        self.gridLayout.addWidget(self.btn_Space, 3, 1, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.widget)
        self.btn_0.setMinimumSize(QtCore.QSize(70, 45))
        self.btn_0.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_0.setFont(font)
        self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 3, 2, 1, 1)
        self.btn_Point = QtWidgets.QPushButton(self.widget)
        self.btn_Point.setMinimumSize(QtCore.QSize(70, 45))
        self.btn_Point.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_Point.setFont(font)
        self.btn_Point.setCheckable(False)
        self.btn_Point.setObjectName("btn_Point")
        self.gridLayout.addWidget(self.btn_Point, 3, 3, 1, 1)
        self.btn_Sure = QtWidgets.QPushButton(self.widget)
        self.btn_Sure.setMinimumSize(QtCore.QSize(70, 45))
        self.btn_Sure.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_Sure.setFont(font)
        self.btn_Sure.setObjectName("btn_Sure")
        self.gridLayout.addWidget(self.btn_Sure, 3, 4, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.widget)
        self.btn_8.setMinimumSize(QtCore.QSize(70, 45))
        self.btn_8.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_8.setFont(font)
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(KeyBoard)
        QtCore.QMetaObject.connectSlotsByName(KeyBoard)

    def retranslateUi(self, KeyBoard):
        _translate = QtCore.QCoreApplication.translate
        KeyBoard.setWindowTitle(_translate("KeyBoard", "KeyBoard"))
        self.label.setText(_translate("KeyBoard", "输入信息："))
        self.btn_Hide.setText(_translate("KeyBoard", "关闭"))
        self.btn_Again.setText(_translate("KeyBoard", "清除"))
        self.btn_Del.setText(_translate("KeyBoard", "←"))
        self.btn_Cap.setText(_translate("KeyBoard", "大写"))
        self.btn_Num.setText(_translate("KeyBoard", "123"))
        self.btn_1.setText(_translate("KeyBoard", "1"))
        self.btn_2.setText(_translate("KeyBoard", "2"))
        self.btn_3.setText(_translate("KeyBoard", "3"))
        self.btn_4.setText(_translate("KeyBoard", "4"))
        self.btn_5.setText(_translate("KeyBoard", "5"))
        self.btn_6.setText(_translate("KeyBoard", "6"))
        self.btn_Sma.setText(_translate("KeyBoard", "小写"))
        self.btn_7.setText(_translate("KeyBoard", "7"))
        self.btn_9.setText(_translate("KeyBoard", "9"))
        self.btn_Wrap.setText(_translate("KeyBoard", "换行"))
        self.btn_Sym.setText(_translate("KeyBoard", "符号"))
        self.btn_Space.setText(_translate("KeyBoard", "└┘"))
        self.btn_0.setText(_translate("KeyBoard", "0"))
        self.btn_Point.setText(_translate("KeyBoard", "."))
        self.btn_Sure.setText(_translate("KeyBoard", "确定"))
        self.btn_8.setText(_translate("KeyBoard", "8"))


