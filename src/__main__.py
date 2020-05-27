from src.soul.Liza import Liza
import src.base.functoins as base

# base.news()
liza = Liza()
liza.hello_msg()
while True:
    liza.say('Я готова выполнить команду')
    liza.listen_and_think()