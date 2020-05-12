from text_query_handlers import AbstractHandler as ah
from datetime import datetime, date, time
import ConstantsAndUtils as cau


class ScheduleHandler(ah.AbstractHandler):
    am_right = {"скарлет", "дай", "розклад"}

    # TODO: move it into some config file
    shedule = {"понеділок": [
        "11:50-13:10 Довкілля(лаб з) (365)",
        "13:30-14:50 Мат економ(лек) (265)"
    ], "вівторок": [
        "16:40-18:00 Політ(лаб з) (366)",
        "16:40-18:00 Політ(лек ч) (265)",
        "18:10-19:30 ЧММФ(пр) (261)",
        "19:40-21:00 Мат економ(прак) (272/3)"
    ], "середу": [
        "13:30-14:50 Крипто(пр) (119а)",
        "15:05-16:25 Крипто(лаб) (119а)",
        "16:40-18:00 Довкілля(лек) (265)"
    ], "четвер": [
        "13:30-14:50 ЧММФ(лек) (265)",
        "15:05-16:25 Мат моделі(лек) (265)",
        "16:40-18:00 Мат моделі(пр) (118а)"
    ], "п'ятницю": [
        "16:40-18:00 Ген алг(лаб з) (118ф)",
        "18:10-19:30 Ген алг(пр) (261)",
        "19:40-21:00 Ген алг(пр) (261)"
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
