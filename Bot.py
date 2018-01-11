import telebot
import re
from random import randint
from datetime import datetime

token = "396392020:AAGeG8wChwfs-t2gXmuh5-Kh67yupIOcpWk"
master_id = 404995725
print("start")
bot = telebot.TeleBot(token)
words_split = r"[\w']+"
greeting_set = set(["привітайся", "скарлет"])
hello_set = set(["привіт", "скарлет"])
gb_set = set(["бувай", "скарлет"])
love_set = set(["ти", "скарлет", "мене", "любиш"])
am_right = set(["хіба", "я", "не", "правий"])


def part_of_day_from_hour(hour):
    part_of_day = ""
    if (hour >= 6 and hour < 12):
        part_of_day = "ранку"
    elif (hour >= 12 and hour < 18):
        part_of_day = "дня"
    elif (hour >= 18 and hour < 23):
        part_of_day = "вечора"
    elif (hour >= 23 or hour < 6):
        part_of_day = "ночі"
    return part_of_day


def in_set(text, your_set):
    return set(map(lambda x: x.lower(), re.findall(words_split, text))) >= your_set


def love_predicate(message):
    return in_set(message.text, love_set)


def love(message, user_name):
    bot.send_message(message.chat.id, "Я люблю тебе ," + user_name + ")")


def greeting_predicate(message):
    return in_set(message.text, greeting_set)


def greeting(message):
    mess = "Привіт , я Скарлет , ваш бот)"
    bot.send_message(message.chat.id, mess)


def random_predicate(message):
    return len(re.findall("(/random\(\d+\))", message.text)) > 0


def random(message, user_name):
    user_name = message.from_user.first_name
    number = randint(0, (int(re.findall("(\d+)", message.text)[0])))
    bot.send_message(message.chat.id, user_name + " викинув " + str(number))


def location_preidcate(message):
    return (message.text == "Де я?") or (message.text == "Where am I?")


def location(message, user_name):
    bot.send_message(message.chat.id, user_name + ": x:(" + message.location + ")" + " y:(" + message.location + ")")


def hello_predicate(message):
    return in_set(message.text, hello_set) or in_set(message.text, gb_set)


def hello(message, user_name):
    hour = datetime.fromtimestamp(message.date).time().hour
    bot.send_message(message.chat.id, datetime.fromtimestamp(message.date))
    part_of_day = part_of_day_from_hour(hour)
    good = ""
    if (part_of_day == "ночі"):
        good = "Доброї"
    else:
        good = "Доброго"
    bot.send_message(message.chat.id, good + " " + part_of_day + " ," + user_name + ")")


def test_pred(message):
    return message.text == "Пінг"


def test(message):
    bot.send_message(message.chat.id, "Понг")


def right_predicate(message):
    return in_set(message.text, am_right) and message.from_user.id == master_id


def right(message):
    bot.send_message(message.chat.id, "Ви праві, господарю)")


@bot.message_handler(content_types=['text'])
def handle_text(message):
    user_name = message.from_user.first_name
    if (love_predicate(message)):
        love(message, user_name)
    elif (greeting_predicate(message)):
        greeting(message)
    elif (random_predicate(message)):
        random(message, user_name)
    elif (hello_predicate(message)):
        hello(message, user_name)
    elif (test_pred(message)):
        test(message)
    elif (right_predicate(message)):
        right(message)


bot.polling(none_stop=True)
