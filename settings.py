# todo make these clickable options to change, need to save and read at start

import requests


class Settings:
    def __init__(self, profile_name, lower_temperature, upper_temperature, earliest_time, latest_time):
        self.profile_name = profile_name
        self.lower_temperature = lower_temperature
        self.upper_temperature = upper_temperature
        self.earliest_time = earliest_time
        self.latest_time = latest_time
        # called token on Air Quality Open Data Platform, my personal key, set for testing only


def set_default():      # fixme use the config feature to load/update
    default_settings = Settings("Default",45,80,"08:00",
                                "21:00")
    return default_settings