from text_query_handlers import AbstractHandler as ah
from datetime import datetime, date, time
import ConstantsAndUtils as cau


class ScheduleHandler(ah.AbstractHandler):
    am_right = {"скарлет", "дай", "розклад"}

    # TODO: move it into some config file
    shedule = {"понеділок": [
        "13:30-14:50 ДО(прак з) (366)",
        "15:05-16:25 ДО(лек) (266)",
        "16:40-18:00 Інтегральні(прак ч) (366)"
    ], "вівторок": [
        "15:05-16:25 Охорона(лек з) (114)",
        "15:05-16:25 Охорона(прак ч) (114)",
        "16:40-18:00 ЧММФ(лек) (265)",
        "18:10-19:30 ЧММФ(прак ч) (261)"
    ], "середу": [
        "13:30-14:50 MO(лек) (265)",
        "15:05-16:25 Геометрія(пр) (266)",
        "16:40-18:00 Геометрія(лаб) (119а)",
        "18:10-19:30 Геометрія(лаб ч) (119а)"
    ], "четвер": [
        "15:05-16:25 ЧММФ(лек ч) (265)",
        "15:05-16:25 Інтегральні(лек з) (265)",
        "16:40-18:00 Інтегральні(лек) (111)"
    ], "п'ятницю": [
        "13:30-14:50 МО(лаб) (266)", 
        "15:05-16:25 Веб(прак) (261)",
        "16:40-18:00 Веб(лаб) (261)"
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
