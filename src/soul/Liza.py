import pyttsx3
import speech_recognition as sr
import os
import src.base.commands as base
from .liza_configs import *


class Liza:

    def __init__(self):
        self.tts = pyttsx3.init()  # Инициализировать голосовой движок.
        self.tts.setProperty('voice', VOICE_ID)

    def hello_msg(self):
        self.say("Привет, я - Лиза! Ваш голосовой помощник!")

    def say(self, message):
        print('Liza say: {0}'.format(message))
        # self.tts.say(message)
        # self.tts.runAndWait()

    def voice_(self, message):
        self.tts.say(message)
        self.tts.runAndWait()

    def listen_and_think(self):
        text = self.listen()
        if text is None:
            self.say('У меня болит голова, давай завтра!')
        else:
            print('Вы сказали: {0}'.format(text))
            if self.think(text) is None:
                self.say('Мне не удалось распознать команду')

    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="ru").lower()
            return text
        # loop back to continue to listen for commands if unrecognizable speech is received
        except sr.UnknownValueError:
            return None

    def think(self, command):
        if 'vk' in command or 'vk.com' in command or 'вк' in command:
            base.open_vk()
            self.say('Открываю бразуер')
        elif 'открой' in command:
            self.say(base.open_browser(command))
        elif 'погода' in command:
            self.say(base.get_whether(command))
        elif 'расскажи мне о' in command:
            self.say(base.search_info(command))
        elif 'новости' in command:
            for news in base.get_news()[:15]:
                self.voice_(news.title.text)
        else:
            return None
