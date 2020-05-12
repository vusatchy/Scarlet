from text_query_handlers import AbstractHandler as ah
import re
from random import randint
import ConstantsAndUtils as cau

class ProxyCallHandler(ah.AbstractHandler):

    match_regex = "(/message: (.*)\n?/id: (.*))"

    def predicate(self, message):
        return len(re.findall(self.match_regex, message.text)) > 0 \
               and message.from_user.id == cau.master_id

    def handle(self, bot, message):
        text = message.text
        mess = re.search(self.match_regex, text).group(2)
        id = re.search(self.match_regex, text).group(3)
        bot.send_message(id, mess)
