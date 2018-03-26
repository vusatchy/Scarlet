from text_query_handlers import AbstractHandler as ah
import ConstantsAndUtils as cau


class LoveHandle(ah.AbstractHandler):
    love_set = {"ти", "скарлет", "мене", "любиш"}

    def predicate(self, message):
        return cau.in_set(message.text, self.love_set)

    def handle(self, bot, message):
        user_name = message.from_user.first_name
        bot.send_message(message.chat.id, "Я люблю тебе ," + user_name + ")")
