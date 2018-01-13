import re

master_id = 404995725
words_split = r"[\w']+"


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
