from configparser import ConfigParser
import os

config = ConfigParser()


def create_ini_file(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            config.write(f)


# create if doesn't exist then read
ini_file = 'weather.ini'
create_ini_file(ini_file)
config.read(ini_file)


config["Settings"] = {
    "weather_profile": "Default_Preferences",
    "time_12": False,
    "scale": "F",    # todo interact w/convert_time in time_calculator
    "key": "",
    "profile": "Default Weight"
}

config["Default Preferences"] = {
    "lower_temperature": 45,
    "lower_temperature2": 35,
    "upper_temperature": 80,
    "upper_temperature2": 85,
    "earliest_time": "08:00",
    # fixme add an option to have two windows that can be weighted the same
    "latest_time": "21:00",
    "humidity": 50,
    "humidity2": 60,
}

config["Morning"] = {
    "lower_temperature": 45,
    "upper_temperature": 80,
    "earliest_time": "06:00",
    "latest_time": "09:00",
}

config["Night"] = {
    "lower_temperature": 45,
    "upper_temperature": 80,
    "earliest_time": "18:00",
    "latest_time": "23:00",
}

config["Default Weight"] = {
    "time_weight": 5,
    "humidity_weight": 4,
    "humidity_weight2": 3,
    "rain_weight": 1,
    "temperature_weight": 4,
    "temperature_weight_2": 2,
    "string": "string"
}


if __name__ == '__main__':
    with open("weather.ini", "w") as f:
        config.write(f)


# Example of reading a setting
# weather_profile = config.get('Settings', 'weather_profile')