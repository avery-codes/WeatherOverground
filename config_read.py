from configparser import ConfigParser

config = ConfigParser()

# try:
config.read('weather.ini')
# except:
#    print("Unable to load preferences.")
#    raise SystemExit()


if __name__ == '__main__':
    with open("weather.ini", "r") as f:
        config.read(f)
