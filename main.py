from time_calculator import Calendars
from weather import (get_nws_api, get_coordinates, get_forecasts, get_aqi_specs)
import customtkinter as ctk
from tabs import create_tabs
from settings import set_default
from ui_elements import tab_frame_config, refresh_button, aqi_button, sorting_button


# todo error handling

global template_tab, tab_1, tab_2, tab_3


def main() -> None:
    ctk.set_appearance_mode("system")
    root = ctk.CTk()
    root.title("Weather Overground")
    WINDOW_WIDTH = 685
    WINDOW_HEIGHT = 600
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")  # main window
    key = ""    #fixme remove key before commit
    aqi_specs = get_aqi_specs(key)     # for aqi display and attribution

    font = ('Helvetica', 16)


    # main frame, entire window
    main_frame = ctk.CTkFrame(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    main_frame.grid()

    # defining main grid
    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(0, weight=1)  # top row
    main_frame.columnconfigure(1, weight=1)
    main_frame.rowconfigure(1, weight=5)  # bottom row

    # title label
    headline = ctk.CTkLabel(main_frame, text="Weather Overground", font=("Helvetica", 24), text_color="white",
                            anchor='center', fg_color="gray16")
    headline.grid(column=0, row=0, pady=10, sticky="nsew")


    # dates, settings, coordinates via IP address
    calendar = Calendars()
    settings = set_default()
    coordinates = get_coordinates()

    # creating nws forecast list
    nws_response = get_nws_api(coordinates)
    try:
        forecasts = get_forecasts(nws_response, settings)
    except TypeError as e:
        print("Forecasts failed to load. Please refresh using the reload button.")

    # tab frame, holds everything except header label
    tab_frame = tab_frame_config(main_frame)

    forecast_frame = ctk.CTkFrame(tab_frame, width=675, height=WINDOW_HEIGHT - 40)
    forecast_frame.grid(row=1, column=0, sticky='nsew')
    create_tabs(forecast_frame, font, forecasts, calendar, key)

    refresh_button(forecast_frame, font, forecasts, calendar, key, tab_frame)

    aqi_button(aqi_specs, tab_frame, font)

    sorting_button(tab_frame, font)

    root.mainloop()

if __name__ == '__main__':
    main()