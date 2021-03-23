# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scene1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie

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
        
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setStyleSheet("background-image:url(img/background.png)")
        Form.setObjectName("Form")
        Form.resize(800, 480)
        self.label_2 = MyQLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 50, 48))
        self.label_2.setObjectName("label_2")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(630, 20, 84, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_4 = MyQLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(740, 10, 47, 43))
        self.label_4.setObjectName("label_4")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(60, 70, 671, 261))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label = MyQLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 360, 800, 120))
        self.label.setObjectName("label")
        self.label_3 = MyQLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(330, 340, 133, 133))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 440, 93, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Scene1"))
        # self.label_3.setText(_translate("Form", "TextLabel"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))

        # self.gif = QMovie("img/solving.gif")
        # self.label_3.setMovie(self.gif)
        # self.label_3.setMinimumHeight(self.label_3.width())
        # self.gif.setScaledSize(self.label_3.size())
        # self.gif.start()

        self.textBrowser.setStyleSheet("QTextBrowser{border-width:0;border-style:outset}")

        pix=QtGui.QPixmap("img/finished.png")
        self.label_3.setPixmap(pix)
        self.label_3.adjustSize()

        pix2=QtGui.QPixmap("img/volume_icon.png")
        self.label_4.setPixmap(pix2)
        self.label_4.adjustSize()

        pix3=QtGui.QPixmap("img/return_icon.png")
        self.label_2.setPixmap(pix3)
        self.label_2.adjustSize() 

        # self.gif = QMovie("img/recording.gif")
        # self.label.setMovie(self.gif)
        # self.label.adjustSize()
        # self.label.lower()
        # self.gif.start()


        # 通过设置不透明度，隐藏管理员按钮
        op = QtWidgets.QGraphicsOpacityEffect()
        # 设置透明度的值，0.0到1.0，最小值0是透明，1是不透明
        op.setOpacity(0)
        self.pushButton_2.setGraphicsEffect(op)