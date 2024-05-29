from preferences import update_settings, print_settings, set_default
from time_calculator import current, week, tomorrow
from weather import get_weather, get_coordinates, get_forecasts, weigh_forecasts  # , print_weather
import customtkinter as ctk
import tkinter as tk
from tkcalendar import Calendar


ctk.set_appearance_mode("system")
root = ctk.CTk()


root.title("Weather Overground")
root.geometry("800x400")  # window size

week = week()


'''
default_settings = set_default()
btn = CTkButton(root, text="button!", command=print_settings(default_settings))
btn.place(anchor="se")
'''

# current date, settings, coordinates via IP address
current = current()
settings = set_default()
coordinates = get_coordinates()

# get all weather forecast data
response = get_weather(coordinates)
forecasts = get_forecasts(response)
# print_weather(forecasts, current, settings)

# title
label = ctk.CTkLabel(root, text=f"Weather Overground", font=("Arial", 22), padx=100,
                     justify="center")
label.pack()

# def print_weather(forecasts, current, settings):
# for each in forecasts:
frame = ctk.CTkScrollableFrame(root, width=300, orientation="vertical")
frame.pack(expand=True, padx=0, pady=0, fill="both")


#        label.pack(anchor="s")
# label.pack(anchor = "center")
# todo change to address, wouldn't need zip stuff with Nominatim
# todo weather
# todo outdoor air quality, pollen count
# todo indoor air quality, link to sensor?
# todo give a few options w/stats to pick from
# todo set a reminder?

'''
# current settings
current_settings = Settings()
print_settings(current_settings)
choice = input("Would you like to update the settings? Y or N     ").lower()   # todo traceback error KeyboardInterrupt
if choice == "y":
    current_settings = update_settings(current_settings)
'''

##########################
# create tabview
my_tab = ctk.CTkTabview(frame, width = 300, height = 500, corner_radius=10,
                        segmented_button_selected_color="forest green")     # fg_color="gray26",

my_tab.pack()

# create tabs
tab_1 = my_tab.add("Today")
tab_2 = my_tab.add("Tomorrow")
tab_3 = my_tab.add("This Week")


# put stuff in tabs

# tab1
label = ctk.CTkLabel(tab_1, text=f"Hourly Weather Window for {week[1]}", font=("Arial", 18), padx=100,
                     justify="center")
label.pack(anchor="nw")
categories = ctk.CTkLabel(tab_1, text="Date\tTime\t    Temp\tHumidity\tRain\tWeight", font=("Arial", 14),
                     justify="center", padx=20).pack()
for i in forecasts:
    hourly = weigh_forecasts(forecasts[i], settings)
    if hourly.date == current[0]:
        label = ctk.CTkLabel(tab_1, text=(f'{hourly.date:10}\t{hourly.start_time:10}\t{hourly.temperature:10}\t'
                            f'{hourly.humidity:10}\t{hourly.rain_chance:10}\t{hourly.weight:10}'),
                            font=("Arial", 16)).pack(expand=False, anchor="nw")


# tab2
tomorrow = tomorrow()

label = ctk.CTkLabel(tab_2, text=f"Hourly Weather Window for {tomorrow}", font=("Arial", 18), padx=100, justify="center")
label.pack(anchor="nw")

categories = ctk.CTkLabel(tab_2, text="Date\tTime\t    Temp\tHumidity\tRain\tWeight", font=("Arial", 14),
                     justify="center", padx=20).pack()
for i in forecasts:
    hourly = weigh_forecasts(forecasts[i], settings)
    if hourly.date == tomorrow:
        label = ctk.CTkLabel(tab_2, text=(f'{hourly.date:10}\t{hourly.start_time:10}\t{hourly.temperature:10}\t'
                            f'{hourly.humidity:10}\t{hourly.rain_chance:10}\t{hourly.weight:10}'),
                            font=("Arial", 16)).pack()

# tab3
label = ctk.CTkLabel(tab_3, text="Hourly Weather Window for This Week", font=("Arial", 18), padx=100, justify="center").pack()
categories = ctk.CTkLabel(tab_3, text="Date\tTime\t    Temp\tHumidity\tRain\tWeight", font=("Arial", 14),
                          justify="center", padx=20).pack()
for i in forecasts:
    hourly = weigh_forecasts(forecasts[i], settings)
    if hourly.date in week:
        label = ctk.CTkLabel(tab_3, text=(f'{hourly.date:10}\t{hourly.start_time:10}\t{hourly.temperature:10}\t'
                            f'{hourly.humidity:10}\t{hourly.rain_chance:10}\t{hourly.weight:10}'),
                            font=("Arial", 16)).pack()

root.mainloop()
# root2.mainloop()

# my_button = ctk.CTkButton(tab_1, text="Click me!")
# my_button.pack(pady=40)