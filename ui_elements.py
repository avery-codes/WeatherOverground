from time_calculator import Calendars
from weather import (get_grid, get_coordinates, get_forecasts, assemble_forecasts, get_aqi_dict, get_aqi,
                     fahrenheit_to_celsius)
import customtkinter as ctk
from tabs import create_tabs
from settings import set_default
from configparser import ConfigParser
import webbrowser


def tab_frame_config(main_grid):
    # tab frame, holds everything except header label
    frame = ctk.CTkFrame(main_grid, width=675, height=550, corner_radius=10)
    frame.grid(row=1, column=0, sticky="nsew")
    frame.rowconfigure(0, weight=1)  # top row
    frame.rowconfigure(1, weight=4)  # top row
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=5)
    frame.columnconfigure(2, weight=1)
    return frame




def refresh_button(forecast_frame, font, forecasts, calendar, key, tab_frame) -> None:
    def refresh(forecast_frame, font, forecasts, calendar, key):
        for widget in forecast_frame.winfo_children():
            widget.destroy()
        create_tabs(forecast_frame, font, forecasts, calendar, key)

    button = ctk.CTkButton(tab_frame, text=f'Refresh Forecasts \U0001F504',
                           command=refresh(forecast_frame, font, forecasts, calendar, key), font=font,
                           fg_color="forest green")
    button.grid(row=0, column=0, sticky='w', padx=5, pady=5)

# ---------------------------------


def aqi_action(aqi):
    def no_action():
        pass

    # ACI button
    if aqi is not None:
        if aqi.color == "yellow":
            aqi_button = ctk.CTkButton(tab_frame_config, text=f'Outdoor AQI: {aqi.designation} {aqi.index}',
                                       command=no_action(), fg_color=aqi.color, text_color='black')
        else:
            aqi_button = ctk.CTkButton(tab_frame_config, text=f'Outdoor AQI: {aqi.designation} {aqi.index}',
                                       command=no_action(), fg_color=aqi.color)
    else:
        aqi_button = ctk.CTkButton(tab_frame_config, text="Sorry, API failed to load.", fg_color="black",
                                   command=no_action())
    aqi_button.grid(row=0, column=0, sticky='e', padx=5, pady=5)

