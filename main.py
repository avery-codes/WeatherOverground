from time_calculator import Calendars
from weather import (get_grid, get_coordinates, get_forecasts, assemble_forecasts, get_aqi_dict, get_aqi,
                     fahrenheit_to_celsius)
import customtkinter as ctk
from tabs import create_tabs
from settings import set_default
from configparser import ConfigParser
import webbrowser
from ui_elements import tab_frame_config


# todo error handling

global template_tab, tab_1, tab_2, tab_3


def main() -> None:

    # settings
    config = ConfigParser()
    #    config.read("weather.ini")
    #   config_data = config["Settings"]


    default_settings = set_default()
    ctk.set_appearance_mode("system")
    root = ctk.CTk()
    root.title("Weather Overground")
    WINDOW_WIDTH = 685
    WINDOW_HEIGHT = 600
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")  # main window
    key = ""
    aqi = get_aqi(key)     # for aqi display and attribution
    font = ('Helvetica', 16)


    # main frame, entire window
    main_grid = ctk.CTkFrame(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    main_grid.grid()

    # defining main grid
    main_grid.columnconfigure(0, weight=1)
    main_grid.rowconfigure(0, weight=1)  # top row
    main_grid.rowconfigure(1, weight=1)  # bottom row

    # title label
    headline = ctk.CTkLabel(main_grid, text="Weather Overground", font=("Arial", 24), text_color="white",
                            anchor='center')
    headline.grid(column=0, row=0, pady=10, sticky="nsew")


    # dates, settings, coordinates via IP address
    calendar = Calendars()
    settings = set_default()
    coordinates = get_coordinates()
    # creating forecast list
    grid_response = get_grid(coordinates)
    try:
        forecasts = get_forecasts(grid_response, settings)
    except Traceback:
        print("Forecasts failed to load. Please refresh using the reload button.")
    forecast_list = assemble_forecasts(calendar, forecasts)

    # tab frame, holds everything except header label
    tab_frame = tab_frame_config(main_grid)

    forecast_frame = ctk.CTkFrame(tab_frame, width=675, height=WINDOW_HEIGHT - 40)
    forecast_frame.grid(row=1, column=0, sticky='nsew')
    create_tabs(forecast_frame, font, forecasts, calendar, key)

    # ---------------------------------
    # refresh button
    def refresh(font):
        for widget in forecast_frame.winfo_children():
            widget.destroy()
        create_tabs(forecast_frame, font, forecasts, calendar, key)


    refresh_button = ctk.CTkButton(tab_frame, text=f'Refresh Forecasts \U0001F504', command=refresh(font), font=font,
                                   fg_color="forest green")
    refresh_button.grid(row=0, column=0, sticky='w', padx=5, pady=5)
    # ---------------------------------


    def aqi_action(aqi):
        def no_action():
            pass

        # ACI button
        if aqi is not None:
            if aqi.color == "yellow":
                aqi_button = ctk.CTkButton(tab_frame, text=f'Outdoor AQI: {aqi.designation} {aqi.index}',
                                           command=no_action(), fg_color=aqi.color, text_color='black')
            else:
                aqi_button = ctk.CTkButton(tab_frame, text=f'Outdoor AQI: {aqi.designation} {aqi.index}',
                                           command=no_action(), fg_color=aqi.color)
        else:
            aqi_button = ctk.CTkButton(tab_frame, text="Sorry, API failed to load.", fg_color="black",
                                       command=no_action())
        aqi_button.grid(row=0, column=0, sticky='e', padx=5, pady=5)



    aqi_action(aqi)

    root.mainloop()



if __name__ == '__main__':
    main()