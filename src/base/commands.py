from .config import *
import src.base.functoins as base
import re


def open_vk():
    url = 'https://www.vk.com'
    base.open_web(url)


def open_browser(command):
    reg_ex = re.search('(.*\t?)открой (.+)', command)
    if reg_ex:
        domain = reg_ex.group(1)
        print(domain)
        url = BASE_URL + domain
        base.open_web(url)
        return 'Открываю бразуер'
    else:
        return 'Не удалось открыть браузер'


def get_whether(command):
    reg_ex = re.search('(.*\t?)погода в (.*)', command)
    if reg_ex:
        city = reg_ex.group(2)
        return base.weather(city)


def search_info(command):
    reg_ex = re.search('(.*\t?)расскажи мне о (.*)', command)
    if reg_ex:
        target = reg_ex.group(2)
        return base.wiki(target)

def get_news():
    return base.news()
