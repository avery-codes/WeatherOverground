import customtkinter as ctk
from weather import assemble_forecasts, get_aqi_dict
from settings_tab import *


def create_tabs(tab_frame, font, forecasts, calendar, key) -> None:
    template_tab = ctk.CTkTabview(tab_frame, width=675, height=500, corner_radius=10,
                                  segmented_button_selected_color="forest green")
    template_tab.grid(row=0, column=0, sticky="nsew")

    forecast_list = assemble_forecasts(calendar, forecasts)

    # create tabs
    tab_1 = template_tab.add("Today")
    tab_2 = template_tab.add("Tomorrow")
    tab_3 = template_tab.add("Three Day")
    tab_4 = template_tab.add("Settings")

    make_tab(tab_1, forecast_list[0], font)
    make_tab(tab_2, forecast_list[1], font)
    make_tab(tab_3, forecast_list[2], font)
    make_settings_tab(tab_4, font, key)


def make_tab(tab, forecast_list, font) -> None:
    headers = ["Date", "Time", "Temp", "Humidity", "Rain", "Weight"]

    frame = ctk.CTkScrollableFrame(tab, width=640, height=450)
    frame.grid(sticky="nsew")

    # printing column headers
    for i, text in enumerate(headers):
        label = ctk.CTkLabel(frame, text=headers[i], font=font, justify="center")
        label.grid(row=0, column=i, sticky='nsew', padx=3, pady=3)
        frame.columnconfigure(i, weight=1)

    # printing forecast rows
    index = 0
    row = 1
    while index < len(forecast_list):
        label_maker(forecast_list[index], row, frame, font)
        index += 1
        row += 1


def label_maker(forecast, row_count, frame, font) -> None:
    labels = [
        (forecast.date, 0),
        (forecast.start_time, 1),
        (forecast.temperature, 2),
        (forecast.humidity, 3),
        (forecast.rain_chance, 4),
        (forecast.weight, 5)
    ]
    for text, column in labels:
        label = ctk.CTkLabel(frame, text=text, font=font)
        label.grid(row=row_count, column=column, sticky='nsew', padx=3, pady=2)


def make_settings_tab(tab, font, key) -> None:
    frame = ctk.CTkScrollableFrame(tab, width=640, height=450)
    frame.grid(sticky="nsew")

    response_dict = get_aqi_dict(key)

    grid_configure(frame, 19)

    # temperature format switch
    temp_scale_toggle(frame, font, 0, 0)    # rows = 0 - 2

    # time format switch
    time_scale_toggle(frame, font, 0, 0)    # 0 - 2

    # API key text entry
    key_entry(frame, font, 6, 0, key)        # rows = 6 - 8

    # profile selection
    profile_select(frame, font, 9, 0)       # 9 - 13

    # save settings button
    save_settings(frame, font, 14, 0)        # 14 - 15

    # cancel setting change button
    cancel_settings(frame, font, 14, 0)  # 16 - 17

    links_display(frame, font, 18, 0, response_dict)    # 18+


