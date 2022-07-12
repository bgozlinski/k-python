from gtts import gTTS
import os
from time import sleep, localtime, strftime
import pyglet


class Asystent:
    def __init__(self):
        self.file_name = "config_file.txt"
        self.temp_voice = "temp.mp3"
        self.timeout = 2

    def read_file(self):
        with open(self.file_name, "r") as input_file:
            file = input_file.read()
            input_file.close()
            return file

    def speak(self, text):
        tts = gTTS(text=text, lang="pl")
        tts.save(self.temp_voice)

        text_to_speach = pyglet.media.load(self.temp_voice, streaming=False)
        text_to_speach.play()
        sleep(self.timeout)
        os.remove(self.temp_voice)

    @staticmethod
    def time_now():
        t = localtime()
        time_now = strftime("%H:%M", t)

        return time_now


if __name__ == "__main__":
    assist = Asystent()
    t = assist.time_now().replace(":", "")
    print(t)

    # assist.speak("przerwa obiadowa")
    # assist.speak("czesc")

    file = assist.read_file().split()
    a = file[0].split("-")
    print(a[0].replace(":", ""))

    print(a[0] < t)
