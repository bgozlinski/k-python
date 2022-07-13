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

    #  get local time
    @staticmethod
    def time_now():
        t = localtime()
        time_now = strftime("%H:%M", t)

        return time_now


def file_convert(temp):

    #  merge two non-time strings
    for i in range(1, len(temp)):
        if ":" not in (temp[i - 1]) and ":" not in temp[i]:
            break
    temp[i-1:i+1] = [" ".join(temp[i-1:i+1])]

    #  split two time-like strings
    new_temp = []
    for i in temp:
        new_temp.append(i.split("-"))

    return new_temp


if __name__ == "__main__":
    assist = Asystent()

    file = assist.read_file().split()
    converted_file = file_convert(file)
    previous_string_to_speak = ''
    end = False

    while True:
        time_now = '09:00'
        # time_now = assist.time_now()
        if time_now >= converted_file[0][0]:
            break

    while True:
        time_now = '17:00'
        # time_now = assist.time_now()
        for i, j in enumerate(converted_file):
            if ':' in j[0]:
                if j[0] <= time_now < j[1]:
                    stop_list = i
                    stop_value = j
                    end = False
                    string_to_speak = converted_file[i+1][0]
                    break

                else:
                    string_to_speak = 'Koniec'
                    end = True

        if end is True:
            assist.speak(string_to_speak)
            break
        if previous_string_to_speak != string_to_speak:
            assist.speak(string_to_speak)
            previous_string_to_speak = string_to_speak
