import sys, os
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer, QThread
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QMovie, QPixmap
from PyQt5.Qt import *

#页面窗口
import scene0 #初始页面s0
import scene1 #显示对话窗口的页面s1
import scene2 #管理员窗口s2
import scene3 #修改配置界面s3
import scene4 #导航导览页面s4
import reboot #确认重启提醒窗口

#语音功能
import get_talk
import config

#软键盘
from keyBoard import KeyBoard

#计时器
import time

#全局变量
timer = QTimer()  #按钮长按计时器
timer2 = QTimer() #页面重置计时器 

class MainUI(): 
    def __init__(self):
        #读取Config文件
        spotid = config.get_spot_id()
        robotid = config.get_robot_id()
        qrcode = config.get_robot_qrcode()
        title1 = config.get_config("DisplayText","title1")
        title2 = config.get_config("DisplayText","title2")
        welcome1 = config.get_config("DisplayText","welcome1")
        welcome2 = config.get_config("DisplayText","welcome2")
        welcome3 = config.get_config("DisplayText","welcome3")
        pix=QtGui.QPixmap(qrcode)
        #页面1：打开时的主界面
        self.s0 = QWidget()
        self.ui0 = scene0.Ui_Form()
        self.ui0.setupUi(self.s0)
        self.ui0.label_2.setPixmap(pix)
        self.ui0.label_2.adjustSize
        self.ui0.label_3.setText("<font color = #ebebeb>"+"ID:"+robotid+"<font>")
        self.ui0.label_3.adjustSize()
        self.ui0.label_4.setText("<font color = #ebebeb size = 10>"+title1+"<font>")
        self.ui0.label_4.adjustSize()
        self.ui0.label_5.setText("<font color = #ebebeb size = 10>"+title2+"<font>")
        self.ui0.label_5.adjustSize()
        
        self.ui0.label_8.setText("<font color = #ebebeb size = 30>"+welcome1+"<font>")
        self.ui0.label_8.raise_()

        self.ui0.label_8.adjustSize()
        self.ui0.label_9.setText("<font color = #ebebeb size = 30>"+welcome2+"<font>")
        self.ui0.label_9.adjustSize()
        self.ui0.label_10.setText("<font color = #ebebeb size = 30>"+welcome3+"<font>")
        self.ui0.label_10.adjustSize()
        # self.ui0.textBrowser.adjustSize()
        #页面1信号与槽
        self.ui0.label.button_clicked_signal.connect(self.OnAnywhereChicked)
        self.ui0.label_7.button_clicked_signal.connect(self.OnAnywhereChicked)
        self.ui0.pushButton.pressed.connect(self.On_pushButton_pressed)
        self.ui0.pushButton.released.connect(self.On_pushButton_release)
        self.ui0.verticalSlider.valueChanged.connect(self.ChangeVolume2)
        self.s0.showFullScreen()
        #页面2：对话窗口界面
        self.s1 = QWidget()
        self.ui1 = scene1.Ui_Form()
        self.ui1.setupUi(self.s1)
        #页面2信号与槽
        self.ui1.pushButton_2.pressed.connect(self.On_pushButton_pressed)
        self.ui1.pushButton_2.released.connect(self.On_pushButton_release)
        self.ui1.label_3.button_clicked_signal.connect(self.StartTalk)
        self.ui1.label.button_clicked_signal.connect(self.StartTalk)
        self.ui1.label_2.button_clicked_signal.connect(self.RefreshPage)
        self.ui1.horizontalSlider.valueChanged.connect(self.ChangeVolume)
        self.ui1.label_4.button_clicked_signal.connect(self.SwitchVolume)
        self.ui1.label.hide()
        self.ui1.horizontalSlider.hide()
        # self.ui1.label.lower()
        self.s1.hide()
        #管理员界面
        self.s2 = QWidget()
        self.ui2 = scene2.Ui_Form()
        self.ui2.setupUi(self.s2)
        self.ui2.pushButton_2.clicked.connect(self.Destroy)
        self.ui2.pushButton.clicked.connect(self.ShowReboot)
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
        # 确认重启提醒窗口
        self.s5 = QWidget()
        self.ui5 = reboot.Ui_Form()
        self.ui5.setupUi(self.s5)
        self.ui5.pushButton.clicked.connect(self.RebootCancel)
        self.ui5.pushButton_2.clicked.connect(self.RebootConfirm)
        self.s5.hide()
        # 导入getTalk
        self.getTalk = None
        # status状态信号
        self.status = "finished"
        # 对话框动画状态切换符号 0表示初始状态 1表示运动过一次 再次运动时切换为0
        # self.moveFlag = 0
        # 建立小键盘
        self.keyboard1 = KeyBoard()
        self.keyboard1.hide()
        self.keyboard1.signalShowText.connect(self.SpotidReciveKeyBoard)
        self.keyboard2 = KeyBoard()
        self.keyboard2.hide()
        self.keyboard2.signalShowText.connect(self.RobotidReciveKeyBoard)
        self.ui3.lineEdit.button_clicked_signal.connect(self.KeyBoard1Event)
        self.ui3.lineEdit_2.button_clicked_signal.connect(self.KeyBoard2Event)
        # 聊天线程
        self.talk_thread = None
        #设置系统音量为最大
        self.VolumeSwitch = 0 #音效控件开关 1为展示 0为隐藏 
        os.system("amixer set Master " + "100" + "%")
        self.ui1.horizontalSlider.setValue(100)
        self.ui0.verticalSlider.setValue(100)

        #UI动画GIF
        self.solvingGif = QMovie("img/solving.gif")
        self.recordingGif = QMovie("img/recording.gif")
        self.finished = QPixmap("img/finished.png")
        
    # 绑定GetTalk
    def bindGetTalk(self, getTalk):
        self.getTalk = getTalk
    
    # 鼠标任意按下触发事件
    def OnAnywhereChicked(self, wake=False):
        self.s1.showFullScreen()
        self.s0.hide()
        timer2.timeout.connect(self.RefreshPage)
        timer2.start(120000)
        if(wake == False):
            self.SetInitFinishedView()

    # 页面重置事件   
    def RefreshPage(self):
        self.s0.showFullScreen()
        self.s1.hide()
        timer2.stop()

    # 根据状态设置按钮动画和文字
    def SetFinishedView(self):
        self.ui1.label.hide()
        self.ui1.label_3.show()
        self.ui1.label_3.setPixmap(self.finished)
        self.ui1.label_3.adjustSize()
        
        
    def SetRecordingView(self):
        self.ui1.label.show()
        self.ui1.label_3.hide()
        self.ui1.label.setMovie(self.recordingGif)
        self.recordingGif.start()
        self.ShowTheQuestion("你说，我在听……")
        
    def SetSolvingView(self):
        self.ui1.label.hide()
        self.ui1.label_3.show()
        self.ui1.label_3.setMovie(self.solvingGif)
        self.solvingGif.start()
        #清空对话框
        self.ui1.textBrowser.clear()
        
    def SetInitFinishedView(self):
        self.ui1.label.hide()
        self.ui1.label_3.setPixmap(self.finished)
        #清空对话框
        self.ui1.textBrowser.clear()
        self.ShowTheQuestion("小主人你好呀，我是小童")
        self.ShowTheQuestion("点击下面那个魔幻的按钮开始和我聊天吧")


    # 隐藏按钮的鼠标长按事件
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
        self.ui0.label_2.adjustSize()
        self.ui0.label_3.setText(robotid)
        self.ui3.lineEdit.setText(spotid)
        self.ui3.lineEdit_2.setText(robotid)

    def ShowReboot(self):
        self.s5.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.s5.show()

    def RebootCancel(self):
        self.s5.hide()

    def RebootConfirm(self):
        os.system("chmod 777 ./reboot.sh && ./reboot.sh")

    #关闭程序
    def Destroy(self):
        self.s0.close()
        self.s1.close()
        self.s2.close()
        self.s3.close()
        self.s5.close()
        self.keyboard1.close()
        self.keyboard2.close()

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
        # 终止录音（当在录音时）
        if self.status == "recording":
            self.getTalk.Stop()
            print("trigger stop when recording")
        # 开始聊天（当无任务在进行时）
        elif self.status == "finished":
            #清空对话框
            self.ui1.textBrowser.clear()
            #执行录音等任务
            self.talk_thread = get_talk.GetTalkThread(self.getTalk)
            self.talk_thread.questionSignal.connect(self.ShowTheQuestion)
            self.talk_thread.answerSignal.connect(self.ShowTheAnswer)
            self.talk_thread.statusSignal.connect(self.GetTheStatus)
            self.talk_thread.start()
        # 终止播放音频（当在播放时）
        elif self.status == "playing":
            self.getTalk.Stop()
            print("trigger stop when solving")
            return
        # 忽略请求（处理网络任务时）
        else:
            return

    #展示回答
    def ShowTheAnswer(self,txt):
            self.ui1.textBrowser.append("<font color = 'white' size = 25>"+txt+"<font>")

    #展示问题
    def ShowTheQuestion(self,txt):
           self.ui1.textBrowser.append("<font color = #969696 size = 25>"+txt+"<font>")

    #接受状态
    def GetTheStatus(self, status):
        print("MainUI get status:{}".format(status))
        self.status = status
        # if status == "finished":
        #     try:
        #         self.talk_thread.quit()
        #     except Exception:
        #         return

        # 判断状态与按钮动画
        if (status == "finished"):
            # self.ui1.label_3.adjustSize()
            # self.ui1.label_3.setPixmap(self.finished)
            self.SetFinishedView()
        elif(status == "recording"):
            # self.ui1.label_3.setMovie(self.recordingGif)
            # # self.recordingGif.setScaledSize(self.ui1.label_3.size())
            # self.recordingGif.start()
            self.SetRecordingView()
        elif(status == "solving"):
            # self.ui1.label_3.setMovie(self.solvingGif)
            # # self.ui1.label_3.setMinimumHeight(self.ui1.label_3.width())
            # # self.solvingGif.setScaledSize(self.ui1.label_3.size())
            # self.solvingGif.start()
            self.SetSolvingView()

    #显示小键盘
    def KeyBoard1Event(self):
        self.keyboard1.show()
        self.keyboard2.hide()

    def KeyBoard2Event(self):
        self.keyboard2.show()
        self.keyboard1.hide()

    #接收键盘返回的文字
    def SpotidReciveKeyBoard(self,str):
        self.ui3.lineEdit.setText(str)

    def RobotidReciveKeyBoard(self,str):
        self.ui3.lineEdit_2.setText(str)

    # 页面2改变音量
    def ChangeVolume(self):
        volume = self.ui1.horizontalSlider.value()
        print(volume)
        os.system("amixer set Master " + str(volume) + "%")

    # 页面1改变音量
    def ChangeVolume2(self):
        volume = self.ui0.verticalSlider.value()
        print(volume)
        os.system("amixer set Master " + str(volume) + "%")

    # 页面2静音按钮
    def SwitchVolume(self):
        # if(self.VolumeSwitch == 1):
        #     os.system("amixer set Master " + "0" + "%")
        #     self.VolumeSwitch = 0
        # elif():
        #     self.ChangeVolume()
        #     self.VolumeSwitch = 1
        if(self.VolumeSwitch == 1):
            self.ui1.horizontalSlider.hide()
            self.VolumeSwitch = 0
        elif(self.VolumeSwitch == 0):
            self.ui1.horizontalSlider.show()
            self.VolumeSwitch = 1


#主运行函数
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main=MainUI()
    getTalk = get_talk.GetTalk(init_enable=False, debugger=True)
    Main.bindGetTalk(getTalk)
    sys.exit(app.exec_())