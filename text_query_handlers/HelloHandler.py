from text_query_handlers import AbstractHandler as ah
import ConstantsAndUtils as cau
from datetime import datetime


class HelloHandler(ah.AbstractHandler):
    hello_set = set(["привіт", "скарлет"])
    gb_set = set(["бувай", "скарлет"])

    def predicate(self, message):
        return cau.in_set(message.text, self.hello_set) or cau.in_set(message.text, self.gb_set)

    def handle(self, bot, message):
        hour = datetime.fromtimestamp(message.date).time().hour
        user_name = message.from_user.first_name
        part_of_day = cau.part_of_day_from_hour(hour)
        good = ""
        if (part_of_day == "ночі"):
            good = "Доброї"
        else:
            good = "Доброго"
        bot.send_message(message.chat.id, good + " " + part_of_day + " ," + user_name + ")")
