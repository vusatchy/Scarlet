import schedule
import telebot

from TaskLoop import TaskLoop
from text_query_handlers import HandlersRegistration as hr

token = "396392020:AAGeG8wChwfs-t2gXmuh5-Kh67yupIOcpWk"
print("start")
bot = telebot.TeleBot(token)

handlers_provider = hr.HandlersRegistration()
handlers_provider.registration()
task_loop = TaskLoop(1,"Thread-1")
task_loop.daemon = True
task_loop.start()

@bot.message_handler(content_types=['text'])
def handle_text(message):
    handlers = handlers_provider.handlers
    for handler in handlers:
        if handler.predicate(message):
            handler.handle(bot, message)
            break


bot.polling(none_stop=True)
