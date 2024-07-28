import customtkinter as ctk
from tabs import create_tabs
from sorting import get_sorting_values


# forest green use '#228B22'


def tab_frame_config(main_grid) -> object:
    # tab frame, holds everything except header label
    frame = ctk.CTkFrame(main_grid, width=675, height=550, corner_radius=10)
    frame.grid(row=1, column=0, sticky="nsew")
    frame.rowconfigure(0, weight=1)  # top row
    frame.rowconfigure(1, weight=4)  # top row
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=5)
    frame.columnconfigure(2, weight=1)
    return frame


def refresh_button(frame, font, forecasts, calendar, key, tab_frame) -> None:
    def refresh(frame, font, forecasts, calendar, key):
        for widget in frame.winfo_children():
            widget.destroy()
        create_tabs(frame, font, forecasts, calendar, key)

    button = ctk.CTkButton(tab_frame, text=f'Refresh Forecasts \U0001F504',
                           command=refresh(frame, font, forecasts, calendar, key), font=font,
                           fg_color="forest green")
    button.grid(row=0, column=0, sticky='w', padx=5, pady=5)


def aqi_button(aqi_specs, frame, font) -> None:
    if aqi_specs is not None:
        if aqi_specs.color == "yellow":
            button = ctk.CTkButton(frame, text=f'Outdoor AQI: {aqi_specs.designation} {aqi_specs.index}',
                                   fg_color=aqi_specs.color, hover_color=aqi_specs.color, text_color='black', font=font)
        else:
            button = ctk.CTkButton(frame, text=f'Outdoor AQI: {aqi_specs.designation} {aqi_specs.index}',
                                   fg_color=aqi_specs.color, hover_color=aqi_specs.color, font=font)
    else:
        button = ctk.CTkButton(frame, text="Sorry, API failed to load.", fg_color='black', hover_color='black',
                               font=font)

    button.grid(row=0, column=0, sticky='ns', padx=5, pady=5)



def sorting_button(frame, font):
    def optionmenu_callback(choice):
        print("optionmenu dropdown clicked:", choice)

    sorting_values = get_sorting_values()

    optionmenu_var = ctk.StringVar(value="Sort results by:")
    optionmenu = ctk.CTkOptionMenu(frame, width=220,
                                   values=sorting_values,
                                   command=optionmenu_callback,
                                   variable=optionmenu_var, fg_color="gray16", button_color="forest green", font=font)
    optionmenu.grid(row=0, column=0, sticky='e', padx=5, pady=5)

    # .get to grab the current string value of optionmenu