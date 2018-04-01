import random

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
phrases = ['Слава Богу','Який жах...','Паскудство !','звучить цікаво, давай спробуємо','Курва мать !','А це законно ?',
           'Навіть не знаю що сказати...','Вибачте, я на селі','Піду кроликів погодую','Як мило...','Щоб я про це більше не чула','Амінь','Мамі своїй це скажи',
           'Я бачила хентай, який починався так само','Натяк зрозуміла ;)','Вийди з групи','А ти знаєш, що мені подобається...','Це мій статус у фейсбуці',
           'Пффффффффффхіхіхіхіхіхі )','Це з якогось аніме ?','Ех, хлопці...','Приїхали...','Ну це не кемільфо','Мені здається ,чи ви знову щось замислили?']

@bot.message_handler(content_types=['text'])
def handle_text(message):
    handlers = handlers_provider.handlers
    for handler in handlers:
        if handler.predicate(message):
            handler.handle(bot, message)
            return
    probability = random.randint(0, 100)
    if probability >=98:
        phrase = phrases[random.randint(0, len(phrases) - 1)]
        bot.send_message(message.chat.id, phrase)




bot.polling(none_stop=True)
