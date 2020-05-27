import webbrowser
from pyowm import OWM
import wikipedia
import urllib.request
from bs4 import BeautifulSoup as soup
from .config import *


def open_web(url):
    webbrowser.open(url)


def nothing():
    pass


def weather(city):
    print(city)
    owm = OWM(API_key=OVM_API_KEY, language="RU")
    obs = owm.weather_at_place(cities[city])
    wthr = obs.get_weather()
    status = wthr.get_status()
    temperature = wthr.get_temperature(unit='celsius')
    return 'Текущая погода в {0} - {1}. Максимальная температура - ' \
           '{2} и минимальная температруа {3} градусов цельсия' \
        .format(city, status, temperature['temp_max'], temperature['temp_min'])


def wiki(target):
    try:
        wikipedia.set_lang("ru")
        ny = wikipedia.summary(target)
        return  ny.content[:500].encode('utf-8')
    except Exception as e:
        print('Что-то пошло не так!')
        return e


def news():
    try:
        Client = urllib.request.urlopen(NEWS_URL)
        xml_page = Client.read()
        Client.close()
        soup_page = soup(xml_page, "lxml")
        news_list = soup_page.findAll("item")
        return news_list
    except Exception as e:
        print(e)