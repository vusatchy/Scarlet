from text_query_handlers import AbstractHandler as ah


class PingHandler(ah.AbstractHandler):
    def predicate(self, message):
        return message.text == "Пінг"

    def handle(self, bot, message):
        bot.send_message(message.chat.id, "Понг")
