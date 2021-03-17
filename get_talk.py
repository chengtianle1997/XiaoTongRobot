import robot_recorder
import robot_speaker
import get_answer
import txt_to_voice
import voice_to_txt
import time
import config
import random
import _thread
from PyQt5.QtCore import QThread, pyqtSignal


class GetTalkThread(QThread):
    # 定义信号
    questionSignal = pyqtSignal(str)
    answerSignal = pyqtSignal(str)
    statusSignal = pyqtSignal(str)

    def __init__(self, getTalk):
        super(GetTalkThread, self).__init__()
        self.getTalk = getTalk

    def run(self):
        self.getTalk.BindSignal(self.questionSignal, self.answerSignal, self.statusSignal)
        self.getTalk.Talk()


class GetTalk:
    def __init__(self, init_enable=False, debugger=False):
        self.recorder = robot_recorder.robot_recorder()
        self.speaker = robot_speaker.robot_speaker()
        self.txt_to_voice = txt_to_voice.txt_to_voice()
        self.voice_to_txt = voice_to_txt.voice_to_txt()
        self.get_answer = get_answer.TuringRobot()
        # 录音状态指示
        self.recording = False
        # 初始化使能
        self.init_enable = init_enable
        # 调试功能使能
        self.debugger = debugger
        # 语音资源文件根目录
        self.audiodir = "resources/"
        # 检查文件配置
        if init_enable:
            self.InitAutoReply()
        # 状态表
        self.status = ["recording", "solving", "playing", "finished"]
        # 当前状态
        self.status_now = "finished"
        # 信号绑定
        self.question_signal = None
        self.answer_signal = None
        self.status_signal = None

    # 绑定信号
    def BindSignal(self, question_signal, answer_signal, status_signal):
        # 信号绑定
        self.question_signal = question_signal
        self.answer_signal = answer_signal
        self.status_signal = status_signal
    
    # 主功能函数：开始聊天
    def Talk(self):
        # 开始录音
        self.set_status(self.status[0])
        self.recording = True
        self.recorder.record()
        self.recording = False
        self.set_status(self.status[1])
        # 语音转文字
        code, txt, error_msg = self.voice_to_txt.convert()
        self.set_question_txt(txt)
        # 错误处理
        if not code == 0:
            if code == 888:
                self.networkerr_sound()
            elif code == 999:
                self.internalerr_sound()
            else:
                self.internalerr_sound()
            if self.debugger:
                print("voice to txt error: code-{}, errmsg-{}".format(code, error_msg))
            self.set_status(self.status[3])
            return
        # 问题转回答
        # 空问题处理
        if txt == '':
            self.internalerr_sound()
            if self.debugger:
                print("voice to txt error: get an empty input text")
            self.set_status(self.status[3])
            return
        code, answer = self.get_answer.get_answer(txt)
        self.set_answer_txt(answer)
        # 错误处理
        if not code == 0:
            if code == 999:
                self.networkerr_sound()
            else:
                self.internalerr_sound()
            if self.debugger:
                print("get answer error: code-{}".format(code))
            self.set_status(self.status[3])
            return
        # 文字转语音
        answer += "。"
        code, error_msg = self.txt_to_voice.convert(answer)
        # 错误处理
        if not code == 0:
            if code == 888:
                self.networkerr_sound()
            elif code == 999:
                self.internalerr_sound()
            else:
                self.internalerr_sound()
            if self.debugger:
                print("txt to voice eror: code-{}, errmsg-{}".format(code, error_msg))
            self.set_status(self.status[3])
            return
        # 播放语音
        self.set_status(self.status[2])
        self.speaker.play("answer.mp3")
        self.set_status(self.status[3])
    
    # 主功能函数：手动停止录音（若录音过程未结束）
    def Stop(self):
        if self.recording:
            self.recorder.stop()
        elif self.status_now == self.status[2]:
            self.speaker.stop()
            self.set_status(self.status[3])
        return

    # 检查并加载预设定语音
    def InitAutoReply(self):
        # 加载欢迎音
        welcome_file = self.audiodir + "welcome.mp3"
        welcome_txt = config.get_config("autoreply", "welcome")
        self.txt_to_voice.convert(welcome_txt, welcome_file)
        # 加载命令提示音
        instr_file = self.audiodir + "instruction.mp3"
        instr_txt = config.get_config("autoreply", "instruction")
        self.txt_to_voice.convert(instr_txt, instr_file)
        # 加载网络错误语音1, 2, 3
        neterr_file_root = self.audiodir + "networkerr"
        for i in range(1, 4):
            neterr_file = neterr_file_root + str(i) + ".mp3"      
            neterr_txt = config.get_config("autoreply", "networkerror" + str(i))
            # 生成预置语音文件
            self.txt_to_voice.convert(neterr_txt, neterr_file)
        # 加载内部错误语音1, 2, 3
        interr_file_root = self.audiodir + "internalerr"
        for i in range(1, 4):
            interr_file = interr_file_root + str(i) + ".mp3"
            interr_txt = config.get_config("autoreply", "internalerror" + str(i))
            # 生成预置语音文件
            self.txt_to_voice.convert(interr_txt, interr_file)
        # 加载唤醒音
        wakeup_file = self.audiodir + "wakeup.mp3"
        wakeup_txt = config.get_config("autoreply", "wakeup")
        self.txt_to_voice.convert(wakeup_txt, wakeup_file)

    # 播放欢迎音
    def welcome_sound(self):
        file_url = self.audiodir + "welcome.mp3"
        welcome_txt = config.get_config("autoreply", "welcome")
        self.set_answer_txt(welcome_txt)
        # _thread.start_new_thread(self.speaker.play, (file_url,))
        self.speaker.play(file_url)

    # 播放命令提示音
    def instruct_sound(self):
        file_url = self.audiodir + "instruction.mp3"
        instr_txt = config.get_config("autoreply", "instruction")
        self.set_answer_txt(instr_txt)
        # _thread.start_new_thread(self.speaker.play, (file_url,))
        self.speaker.play(file_url)

    # 播放网络错误提示音
    def networkerr_sound(self):
        n = random.randint(1, 3)
        file_url = self.audiodir + "networkerr" + str(n) + ".mp3"
        neterr_txt = config.get_config("autoreply", "networkerror" + str(n))
        self.set_answer_txt(neterr_txt)
        # _thread.start_new_thread(self.speaker.play, (file_url,))
        self.set_status(self.status[2])
        self.speaker.play(file_url)
    
    # 播放内部错误提示音
    def internalerr_sound(self):
        n = random.randint(1, 3)
        file_url = self.audiodir + "internalerr" + str(n) + ".mp3"
        interr_txt = config.get_config("autoreply", "internalerror" + str(n))
        self.set_answer_txt(interr_txt)
        # _thread.start_new_thread(self.speaker.play, (file_url,))
        self.set_status(self.status[2])
        self.speaker.play(file_url)

    # 播放唤醒音
    def wakeup_sound(self):
        file_url = self.audiodir + "wakeup.mp3"
        # _thread.start_new_thread(self.speaker.play, (file_url,))
        self.speaker.play(file_url)

    # 设定问题文字
    def set_question_txt(self, question_txt):
        if self.debugger:
            print(question_txt)
        if self.question_signal == None:
            return
        self.question_signal.emit(question_txt)

    # 设定回答文字
    def set_answer_txt(self, answer_txt):
        if self.debugger:
            print(answer_txt)
        if self.answer_signal == None:
            return
        self.answer_signal.emit(answer_txt)

    # 设定当前状态
    def set_status(self, status):
        self.status_now = status
        if self.debugger:
            print("status:{}".format(status))
        if self.question_signal == None:
            return
        self.status_signal.emit(status)

# Test Demo (No Signal Version)
if __name__ == '__main__':
    
    # 获取实例
    getTalk = GetTalk(init_enable=False, debugger=True)
    # 开始聊天
    getTalk.Talk()
    # 保持程序运行（主线程关闭，子线程随之关闭）
    time.sleep(20)
    # 测试手动停止
    # time.sleep(2)
    # getTalk.Stop()
    print("测试结束")
    
    '''
    # 测试提示音
    # 获取实例（使能初始化选项）
    getTalk = GetTalk(init_enable=True, debugger=True)
    getTalk.wakeup_sound()
    time.sleep(4)
    print("测试结束")
    '''