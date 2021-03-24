# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scene0.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QCursor

#自定义带按键功能的label
class MyQLabel(QtWidgets.QLabel):
    # 自定义信号, 注意信号必须为类属性
    button_clicked_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(MyQLabel, self).__init__(parent)

    def mouseReleaseEvent(self, QMouseEvent):
        self.button_clicked_signal.emit()
        
    # 可在外部与槽函数连接
    def connect_customized_slot(self, func):
        self.button_clicked_signal.connect(func)

#自定义带按键功能的TextBrowser
class MyQTextBrowser(QtWidgets.QTextBrowser):
    # 自定义信号, 注意信号必须为类属性
    button_clicked_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(MyQTextBrowser, self).__init__(parent)
 
    def mouseReleaseEvent(self, QMouseEvent):
        self.button_clicked_signal.emit()
        
    # 可在外部与槽函数连接
    def connect_customized_slot(self, func):
        self.button_clicked_signal.connect(func)


class Ui_Form(object):
    def setupUi(self, Form):
        # Form.setStyleSheet("background-image:url(img/background.png)")
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("img/background.png")))
        Form.setPalette(palette)
        Form.setObjectName("Form")
        Form.resize(800, 480)
        pixmap = QtGui.QPixmap('img/touch_cursor.png')
        cursor = QCursor(pixmap)
        Form.setCursor(cursor)

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(210, 150, 280, 35))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(605, 200, 16, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 50, 480, 48))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(550, 20, 165, 165))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = MyQLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 280, 140, 137))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(730, 417, 61, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.verticalSlider = QtWidgets.QSlider(Form)
        self.verticalSlider.setGeometry(QtCore.QRect(750, 70, 22, 84))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.label_6 = MyQLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(740, 10, 47, 43))
        self.label_6.setObjectName("label_6")
        self.label_7 = MyQLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(225, 257, 473, 203))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(260, 280, 72, 15))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(260, 340, 72, 15))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(260, 400, 72, 15))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Scene0"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.label_2.setText(_translate("Form", "TextLabel"))
        self.label_3.setText(_translate("Form", "TextLabel"))

        pix=QtGui.QPixmap("img/text_icon.png")
        self.label_7.setPixmap(pix)
        self.label_7.adjustSize()

        pix2=QtGui.QPixmap("img/volume_icon.png")
        self.label_6.setPixmap(pix2)
        self.label_6.adjustSize()
        
        pix=QtGui.QPixmap("img/logo.png")
        self.label.setPixmap(pix)
        self.label.setGeometry(self.label.x(),self.label.y(),158,158)
        self.label.setScaledContents(True)

        #通过设置不透明度，隐藏管理员按钮
        op = QtWidgets.QGraphicsOpacityEffect()
        # 设置透明度的值，0.0到1.0，最小值0是透明，1是不透明
        op.setOpacity(0)
        self.pushButton.setGraphicsEffect(op)

        # pe = QPalette()
        # pe.setColor(QPalette.WindowText,Qt.red)#设置字体颜色
        # self.label_8.setAutoFillBackground(False)#设置背景充满，为设置背景颜色的必要条件
        # pe.setColor(QPalette.Window,Qt.red)#设置背景颜色
        # #pe.setColor(QPalette.Background,Qt.blue)<span style="font-family: Arial, Helvetica, sans-serif;">#设置背景颜色，和上面一行的效果一样
        # self.label_8.setPalette(pe)
        self.label_8.raise_()