import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer, QThread
from PyQt5 import QtGui, QtCore

import scene0 #初始页面s0
import scene1 #显示对话窗口的页面s1
import scene2 #管理员窗口s2
import scene3 #修改配置界面s3
import scene4 #导航导览页面s4

import get_talk
import config

#全局变量
timer = QTimer()  #按钮长按计时器
timer2 = QTimer() #页面重置计时器 

class MainUI: 
    def __init__(self):
        #读取Config文件
        spotid=config.get_spot_id()
        robotid=config.get_robot_id()
        qrcode=config.get_robot_qrcode()
        pix=QtGui.QPixmap(qrcode)
        #页面1：打开时的主界面
        self.s0 = QWidget()
        self.ui0 = scene0.Ui_Form()
        self.ui0.setupUi(self.s0)
        self.ui0.label_2.setPixmap(pix)
        self.ui0.label_2.adjustSize
        self.ui0.label_3.setText(robotid)
        #页面1信号与槽
        self.ui0.label.button_clicked_signal.connect(self.OnAnywhereChicked)
        self.ui0.textBrowser.button_clicked_signal.connect(self.OnAnywhereChicked)
        self.ui0.pushButton_2.clicked.connect(self.OnAnywhereChicked)
        self.ui0.pushButton_3.clicked.connect(self.ShowMap)
        self.ui0.pushButton.pressed.connect(self.On_pushButton_pressed)
        self.ui0.pushButton.released.connect(self.On_pushButton_release)
        self.s0.showFullScreen()
        #页面2：对话窗口界面
        self.s1 = QWidget()
        self.ui1 = scene1.Ui_Form()
        self.ui1.setupUi(self.s1)
        #页面2信号与槽
        self.ui1.pushButton_2.pressed.connect(self.On_pushButton_pressed)
        self.ui1.pushButton_2.released.connect(self.On_pushButton_release)
        self.ui1.label_3.button_clicked_signal.connect(self.StartTalk)
        self.ui1.pushButton.clicked.connect(self.RefreshPage)
        self.s1.hide()
        #管理员界面
        self.s2 = QWidget()
        self.ui2 = scene2.Ui_Form()
        self.ui2.setupUi(self.s2)
        self.ui2.pushButton_2.clicked.connect(self.Destroy)
        self.s2.hide()
        #修改配置界面
        self.s3 = QWidget()
        self.ui3 = scene3.Ui_Form()
        self.ui3.setupUi(self.s3)
        self.ui3.pushButton.clicked.connect(self.SaveConfig)
        self.ui3.pushButton_2.clicked.connect(self.s3.hide)
        self.ui2.pushButton_3.clicked.connect(self.ShowConfigMenu)
        self.ui3.lineEdit.setText(spotid)
        self.ui3.lineEdit_2.setText(robotid)
        self.s3.hide()
        #导航导览界面
        self.s4 = QWidget()
        self.ui4 = scene4.Ui_Form()
        self.ui4.setupUi(self.s4)
        self.ui4.pushButton.clicked.connect(self.BackToMain)
        self.s4.hide()
        # 导入getTalk
        self.getTalk = None
        # status状态信号
        self.status = "finished"
        
    # 绑定GetTalk
    def bindGetTalk(self, getTalk):
        self.getTalk = getTalk
    
    #鼠标任意按下触发事件
    def OnAnywhereChicked(self):
        self.s1.showFullScreen()
        self.s0.hide()
        timer2.timeout.connect(self.RefreshPage)
        timer2.start(60000)

    #页面重置事件   
    def RefreshPage(self):
        self.s0.showFullScreen()
        self.s1.hide()
        timer2.stop()

    #显示地图界面
    def ShowMap(self):
        self.s4.showFullScreen()
        self.s0.hide()

    #返回主界面（从导航导览）
    def BackToMain(self):
        self.s0.showFullScreen()
        self.s4.hide()


    #隐藏按钮的鼠标长按事件
    def On_pushButton_pressed(self):
        timer.timeout.connect(self.PressEvent)
        timer.start(2000)

    def PressEvent(self):
        self.s2.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.s2.show()
        timer.stop()

    def On_pushButton_release(self):
        timer.stop()

    #显示修改配置页面
    def ShowConfigMenu(self):
        self.s3.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.RefreshUI()
        self.s3.show()

    #修改配置后刷新UI
    def RefreshUI(self):
        spotid=config.get_spot_id()
        robotid=config.get_robot_id()
        qrcode=config.get_robot_qrcode()
        pix=QtGui.QPixmap(qrcode)
        self.ui0.label_2.setPixmap(pix)
        self.ui0.label_2.adjustSize
        self.ui0.label_3.setText(robotid)
        self.ui3.lineEdit.setText(spotid)
        self.ui3.lineEdit_2.setText(robotid)

    #关闭程序
    def Destroy(self):
        self.s0.close()
        self.s1.close()
        self.s2.close()

    #重启程序
    def Restart(self):
        print("重启成功")

    #保存配置文件
    def SaveConfig(self):
        spotid = self.ui3.lineEdit.text()
        config.set_spot_id(spotid)
        robotid = self.ui3.lineEdit_2.text()
        config.set_robot_id(robotid)
        self.RefreshUI()
        self.s3.close()
        print("保存成功")

    #点击对话按钮事件   
    def StartTalk(self):
        if self.status == "recording":
            self.getTalk.Stop()
            print("trigger stop")
        elif self.status == "finished":
            self.talk_thread = get_talk.GetTalkThread(self.getTalk)
            self.talk_thread.questionSignal.connect(self.ShowTheQuestion)
            self.talk_thread.answerSignal.connect(self.ShowTheAnswer)
            self.talk_thread.statusSignal.connect(self.GetTheStatus)
            self.talk_thread.start()
        else:
            return

    #展示回答
    def ShowTheAnswer(self,txt):
        self.ui1.textBrowser.setText(txt)

    #展示问题
    def ShowTheQuestion(self,txt):
        self.ui1.textBrowser_2.setText(txt)

    #接受状态
    def GetTheStatus(self, status):
        print(status)
        self.status = status


#主运行函数
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main=MainUI()
    getTalk = get_talk.GetTalk(init_enable=False, debugger=True)
    Main.bindGetTalk(getTalk)
    sys.exit(app.exec_())
    




        

