from text_query_handlers import AbstractHandler as ah
from datetime import datetime, date, time
import ConstantsAndUtils as cau


class ScheduleHandler(ah.AbstractHandler):
    am_right = {"скарлет", "дай", "розклад"}

    # TODO: move it into some config file
    shedule = {"понеділок": [
        "11:50-13:10 Філософія(лек) (266)",
        "13:30-14:50 Оптика(лек) (365)",
        "15:05-16:25 Оптика(прак) (261)",
        "16:40-18:00 ЧМ(прак) (261,265)"
    ], "вівторок": [
        "15:05-16:25 ЧМ(лек з) (111)",
        "16:40-18:00 ЧМ(лек) (111)",
        "18:10-19:30 Філософія(прак ч) (150)"
    ], "середу": [
        "13:30-14:50 MO(прак з) (117)",
        "15:05-16:25 БД(лек) (266)",
        "16:40-18:00 БД(прак) (365)"
    ], "четвер": [
        "15:05-16:25 MCC(прак ч) (367)",
        "15:05-16:25 MO(лек з) (111)",
        "16:40-18:00 MCC(лек) (265)"
    ], "п'ятницю": [
        "11:50-13:10 QA(пр) (261)",
        "13:30-14:50 QA(лаб) (261)"
    ]}

    def predicate(self, message):
        return cau.in_set(message.text, self.am_right)

    def handle(self, bot, message):
        keys = list(self.shedule.keys())
        pointer = datetime.now().weekday()
        if cau.in_set(message.text, {"сьогодні"}):
            if pointer in range(len(keys)):
                key = keys[pointer]
                self.send_message_by_day(bot, message, key)
                return
        elif cau.in_set(message.text, {"завтра"}):
            pointer = pointer + 1
            if pointer in range(len(keys)):
                key = keys[pointer]
                self.send_message_by_day(bot, message, key)
                return
        elif cau.in_set(message.text, {"вчора"}):
            pointer = pointer - 1
            if pointer in range(len(keys)):
                key = keys[pointer]
                self.send_message_by_day(bot, message, key)
                return

        for key in keys:
            if cau.in_set(message.text, {key}):
                self.send_message_by_day(bot, message, key)
                return

    def send_message_by_day(self, bot, message, key):
        mess = ""
        for word in self.shedule[key]:
            mess = mess + word + "\n"
        bot.send_message(message.chat.id, mess)
