from text_query_handlers import AbstractHandler as ah
import ConstantsAndUtils as cau


class GreetingHandler(ah.AbstractHandler):
    greeting_set = {"привітайся", "скарлет"}

    def predicate(self, message):
        return cau.in_set(message.text, self.greeting_set)

    def handle(self, bot, message):
        mess = "Привіт , я Скарлет , ваш бот)"
        bot.send_message(message.chat.id, mess)
