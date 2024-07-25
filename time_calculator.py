from datetime import datetime, timedelta


class Calendars:
    def __init__(self):
        self.current = datetime.now()
        self.today = self.current.strftime("%m-%d")
        self.currentTime = self.current.strftime("%H:%M")
        self.tomorrow = (datetime.now() + timedelta(days=1)).strftime("%m-%d")
        self.day_after = (datetime.now() + timedelta(days=2)).strftime("%m-%d")
        self.stop_date = (datetime.now() + timedelta(days=3)).strftime("%m-%d")


def convert_time(time_12, hour) -> str:     # fixme is it a string??
    if time_12:
        if hour > 12:
            hour = hour - 12
            return hour