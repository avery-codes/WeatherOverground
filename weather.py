import requests
import customtkinter as ctk


# User-Agent: (myweatherapp.com, contact@myweatherapp.com)
app = ctk.CTk()


class Forecast:
    def __init__(self, start_time, end_time, temperature, humidity, rain_chance):
        self.date = start_time[5:10]
        self.start_time = start_time[11:16]
        self.end_time = end_time[11:16]
        self.temperature = temperature
        self.humidity = humidity
        self.rain_chance = rain_chance
        self.weight = 0

    def __repr__(self):
        return (f"({self.date}, {self.start_time}, {self.end_time}, {self.temperature}, {self.humidity}, "
                f"{self.rain_chance}, {self.weight})")


def get_coordinates():
    # location
    ip_address = requests.get('http://api.ipify.org').text
    geo_data = requests.get(f'http://ip-api.com/json/{ip_address}').json()
    coordinates = [geo_data['lat'], geo_data['lon']]
    return coordinates


def get_weather(coordinates):
    # requesting grid info via lat and long
    response = requests.get(f'https://api.weather.gov/points/{coordinates[0]},{coordinates[1]}/').json()
    # grid data
    grid_id = response['properties']['gridId']
    grid_x = response['properties']['gridX']
    grid_y = response['properties']['gridY']

    # hourly forecast
    response = requests.get(f'https://api.weather.gov/gridpoints/{grid_id}/{grid_x},{grid_y}/forecast/hourly').json()
    return response


def get_forecasts(response):
    forecasts = {}
    number = 0

    for each in response['properties']['periods']:
        forecasts[number] = Forecast(each['startTime'], each['endTime'], each['temperature'],
                                     each['relativeHumidity']['value'], each['probabilityOfPrecipitation']['value'])
        number += 1
    return forecasts


def weigh_forecasts(forecast, settings):
    #  print(forecast.date)
    if ((settings.earliest_time[:2] <= forecast.start_time[:2]) and
            (forecast.start_time[:2] <= settings.latest_time[:2])):
        forecast.weight = forecast.weight + 5
    if int(forecast.humidity) <= 50:
        forecast.weight = int(forecast.weight) + 4
    elif int(forecast.humidity) <= 60:
        forecast.weight = int(forecast.weight) + 3
    if int(forecast.rain_chance) <= 25:
        forecast.weight = int(forecast.weight + 1)
    if int(forecast.temperature >= settings.lower_temperature):
        if int(forecast.temperature <= settings.upper_temperature):
            forecast.weight = int(forecast.weight + 4)
    elif int(forecast.temperature) <= settings.upper_temperature + 10:
        forecast.weight = int(forecast.weight + 2)
    elif int(forecast.temperature) <= settings.lower_temperature - 10:
        forecast.weight = int(forecast.weight + 2)
    return forecast


'''
def weather_sort(forecast):
    for i in range(1, len(forecast)):
        value = forecast.weight[i]
        j = i - 1
        while j >= 0 and value < forecast.weight[j]:
            forecast.weight[j + 1] = forecast.weight[j]
            j -= 1
        forecast.weight[j + 1] = value
    return forecast


def print_weather(forecasts, current, settings):
    # for each in forecasts:
    for i in forecasts:
        hourly = weigh_forecasts(forecasts[i], settings)
        if hourly.date == current[0]:
            print(f'{hourly.date}\t{hourly.start_time}\t\tTemperature:\t{hourly.temperature}°F\t\t'
                              f'Humidity:\t'f'{hourly.humidity}%\t\tRain Chance:\t{hourly.rain_chance}%\t\tWeight:'
                              f'\t{hourly.weight}')
            # label = tk.CTkLabel(app, text=weather_string)
            # label.pack()
'''