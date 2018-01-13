from text_query_handlers import AbstractHandler as ah
import ConstantsAndUtils as cau


class RightHandler(ah.AbstractHandler):
    am_right = set(["хіба", "я", "не", "правий"])

    def predicate(self, message):
        return cau.in_set(message.text, self.am_right) and message.from_user.id == cau.master_id

    def handle(self, bot, message):
        bot.send_message(message.chat.id, "Ви праві, господарю)")
