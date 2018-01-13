from text_query_handlers import AbstractHandler as ah
import re
from random import randint


class RandomHandle(ah.AbstractHandler):
    def predicate(self, message):
        return len(re.findall("(/random\(\d+\))", message.text)) > 0

    def handle(self, bot, message):
        user_name = message.from_user.first_name
        number = randint(0, (int(re.findall("(\d+)", message.text)[0])))
        bot.send_message(message.chat.id, user_name + " викинув " + str(number))
