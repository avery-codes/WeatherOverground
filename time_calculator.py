from datetime import datetime, date, timedelta


def current():
    time = datetime.now()
    current_time = {0: time.strftime("%m-%d"), 1: time.strftime("%H:%M")}
    return current_time


def tomorrow():
    time = datetime.now()
    tomorrow = time + timedelta(days=1)
    tomorrow = tomorrow.strftime("%m-%d")
    return tomorrow


def week():
    this_week = []
    for i in range(7):
        day_plus = (date.today() + timedelta(days=i))
        formatted = day_plus.strftime("%m-%d")
        this_week.append(f"{formatted}")
    return this_week