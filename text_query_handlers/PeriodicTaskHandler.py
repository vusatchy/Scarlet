import re
import schedule

from text_query_handlers import AbstractHandler as ah
import ConstantsAndUtils as cau


def task(chat_id, message, bot):
    bot.send_message(chat_id, message)


class PeriodicTaskHandler(ah.AbstractHandler):
    applic_set = {'скарлет', 'щодня', 'нагадуй'}
    tasks = {}
    task_counter = 0

    def predicate(self, message):
        return cau.in_set(message.text, self.applic_set)

    def handle(self, bot, message):
        text = message.text
        chat_id = message.chat.id
        time = "12:00"
        times = re.findall("(\d{2}:\d{2})", text)
        if len(times) > 0:
            time = times[0]
        phrase = text
        phrases = re.findall("(\"\w+\")", text)
        if len(phrases) > 0:
            phrase = phrases[0].replace('"',"")
        self.task_counter = self.task_counter + 1
        job = schedule.every()
        job.day.at(time).do(task, chat_id, phrase, bot)
        self.tasks[self.task_counter] = job
        bot.send_message(chat_id, "Задача збережена успішно")

    def task(self, chat_id, message, bot):
        bot.send_message(chat_id, message)
