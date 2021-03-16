# from playsound import playsound

# def play_sound(filename):
#     playsound(filename)

from pygame import mixer
import time
from mutagen.mp3 import MP3

class robot_speaker():
    def __init__(self):
        self.bitrate = 16000
        mixer.init(self.bitrate)
        self.stop_sign = False
    
    def play(self, filename):
        self.stop_sign = False
        try:
            mixer.music.load(filename)
            audio = MP3(filename)
            mixer.music.play()
            start_time = time.time()
            # time.sleep(audio.info.length + 1)
            while(time.time() - start_time < (audio.info.length + 1) and not self.stop_sign):
                time.sleep(0.1)
            mixer.music.stop()
        except Exception as e:
            print(e)
            return
    
    def stop(self):
        self.stop_sign = True


# audio = MP3('answer.mp3')
# mixer.init(16000)
# mixer.music.load('answer.mp3')
# mixer.music.play()
# time.sleep(audio.info.length + 1)
# mixer.music.stop()

# Test Demo
if __name__ == '__main__':
    Speaker = robot_speaker()
    Speaker.play('answer.mp3')
