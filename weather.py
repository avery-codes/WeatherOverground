import requests
# import customtkinter as ctk

#
# app = ctk.CTk()


class Forecast:
    def __init__(self, start_time, end_time, temperature, humidity, rain_chance):
        self.date = str(start_time[5:10])
        self.start_time = start_time[11:16]
        self.end_time = end_time[11:16]
        self.temperature = temperature
        self.humidity = humidity
        self.rain_chance = rain_chance
        self.weight = int(1)

    def __repr__(self):
        return (f"({self.date}, {self.start_time}, {self.end_time}, {self.temperature}, {self.humidity}, "
                f"{self.rain_chance}, {self.weight})")


def get_coordinates() -> tuple[float, float]:
    ip_address = requests.get('http://api.ipify.org').text
    geo_data = requests.get(f'http://ip-api.com/json/{ip_address}').json()
    coordinates = (float(geo_data['lat']), float(geo_data['lon']))
    return coordinates


def get_grid(coordinates):  # returns requests.get...json
    response = requests.get(f'https://api.weather.gov/points/{coordinates[0]},{coordinates[1]}/').json()
    grid_id = response['properties']['gridId']
    grid_x = response['properties']['gridX']
    grid_y = response['properties']['gridY']
    response = requests.get(f'https://api.weather.gov/gridpoints/{grid_id}/{grid_x},{grid_y}/forecast/hourly').json()
    return response


def get_forecasts(response, settings) -> list[Forecast]:
    forecasts = []

    for each in response['properties']['periods']:
        forecast = Forecast(each['startTime'], each['endTime'], each['temperature'], each['relativeHumidity']['value'],
                            each['probabilityOfPrecipitation']['value'])
        forecast.weight = weigh_forecasts(forecast, settings)
        forecasts.append(forecast)

    return forecasts


def weigh_forecasts(forecast, settings) -> int:     # fixme use the config feature to load/update
    forecast_weight = int(1)

    if ((settings.earliest_time[:2] <= forecast.start_time[:2]) and
            (forecast.start_time[:2] <= settings.latest_time[:2])):
        forecast_weight += 5
    if int(forecast.humidity) <= 50:
        forecast_weight += 4
    elif int(forecast.humidity) <= 60:
        forecast_weight += 3
    if int(forecast.rain_chance) <= 25:
        forecast_weight += 1
    if settings.lower_temperature <= int(forecast.temperature) <= settings.upper_temperature:
        forecast_weight += 4
    elif int(forecast.temperature) <= settings.upper_temperature + 10:
        forecast_weight += 2
    elif int(forecast.temperature) <= settings.lower_temperature - 10:
        forecast_weight += 2
    return forecast_weight


def assemble_forecasts(calendar, forecasts) -> list[list]:
    forecast_today = []
    forecast_tomorrow = []
    forecast_three_day = []
    count = 0

    while count <= 72:
        if forecasts[count].date == calendar.today:
            forecast_today.append(forecasts[count])
            forecast_three_day.append(forecasts[count])
        elif forecasts[count].date == calendar.tomorrow:
            forecast_tomorrow.append(forecasts[count])
            forecast_three_day.append(forecasts[count])
        elif forecasts[count].date == calendar.day_after:
            forecast_three_day.append(forecasts[count])
        count += 1

    forecast_list = [forecast_today, forecast_tomorrow, forecast_three_day]
    return forecast_list


def get_aqi_dict(key) -> dict:
    # https://aqicn.org/json-api/doc/#api-Geolocalized_Feed-GetHereFeed
    request_address = f'https://api.waqi.info/feed/here/?token={key}'
    response = requests.get(request_address)
    response_dict = response.json()
    return response_dict


class AQI:
    def __init__(self, index, color, designation):
        self.index = index
        self.color = color
        self.designation = designation


class AQI_ATTRIBUTIONS:
    def __init__(self, attributions):
        self.url = attributions[0]
        self.name = attributions[1]



def get_aqi(key) -> AQI:
    aqi_dict = get_aqi_dict(key)
    aqi = aqi_dict["data"]["aqi"]
    aqi = int(aqi)
    color = 'black'
    designation = 'Error'
    current_aqi = AQI(aqi, color, designation)

    if aqi is not None:
        if aqi >= 301:
            current_aqi.color = 'red4'
            current_aqi.designation = "Hazardous"
        elif aqi >= 200:
            current_aqi.color = 'purple3'
            current_aqi.designation = "Very Unhealthy"
        elif aqi >= 151:
            current_aqi.color = 'red2'
            current_aqi.designation = "Unhealthy"
        elif aqi >= 101:
            current_aqi.color = 'dark orange'
            current_aqi.designation = "Unhealthy for Some"
        elif aqi >= 51:
            current_aqi.color = 'yellow'
            current_aqi.designation = "Moderate"
        else:
            current_aqi.color = 'green'
            current_aqi.designation = "Good"
        return current_aqi


def fahrenheit_to_celsius(temperature) -> float:
    celsius_temperature = (temperature - 32.0) * (5/9)
    celsius_temperature = round(celsius_temperature, 1)
    return celsius_temperature


# fixme:
def clock_to_ampm() -> None:
    pass