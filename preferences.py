# todo make these clickable options to change, need to save and read at start


class Settings:
    def __init__(self, profile_name, lower_temperature, upper_temperature, earliest_time, latest_time, scale):
        self.profile_name = profile_name
        self.lower_temperature = lower_temperature
        self.upper_temperature = upper_temperature
        self.earliest_time = earliest_time
        self.latest_time = latest_time
        self.scale = scale


def update_settings(settings):
    # temperature preferences
    print(f'The current preferred coolest temperature is {settings.lower_temperature}°{settings.scale}.')
    choice = input("Would you like to change it? Y or N     ").lower()
    if choice == "y":
        settings.lower_temperature = input("New coolest temperature:    ")
    print(f'The current preferred warmest temperature is {settings.upper_temperature}°{settings.scale}. '
          f'Would you like to change it?')
    choice = input("Would you like to change it? Y or N    ").lower()
    if choice == "y":
        settings.upper_temperature = input("New warmest temperature:    ")

    # time preferences
    print(f'The default earliest start time is {settings.earliest_time}.')
    choice = input("Would you like to change it? Y or N    ").lower()
    if choice == "y":
        settings.earliest_time = input("Preferred earliest time:    ").upper()
    print(f'The default earliest time is {settings.latest_time}.')
    choice = input("Would you like to change it? Y or N    ").lower()
    if choice == "y":
        settings.latest_time = input("Preferred earliest time:    ").upper()

    return settings


def print_settings(settings):
    print(f'Coolest temperature: {settings.lower_temperature}°{settings.scale}.')
    print(f'Warmest temperature: {settings.upper_temperature}°{settings.scale}.')
    print(f'Earliest start time: {settings.earliest_time}.')
    print(f'Latest start time: {settings.latest_time}.')
    return settings


def set_default():
    default_settings = Settings("Default",45,80,"08:00",
       "21:00", "F")
    return default_settings