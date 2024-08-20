import customtkinter as ctk
import webbrowser


def row_spacer(frame, font, row, column) -> None:
    label = ctk.CTkLabel(frame, text='\n', font=font)
    label.grid(row=row, column=column, sticky='nsew', padx=5)


def label_text(frame, text, font, row, column) -> None:
    label = ctk.CTkLabel(frame, text=text, font=font)
    label.grid(row=row, column=column, sticky='w', padx=5)


def grid_configure(frame, total_rows) -> None:
    # columns
    frame.columnconfigure(0, weight=1)

    # rows
    row = 0
    while row < total_rows:
        frame.rowconfigure(row, weight=1)
        row += 1


def temp_scale_toggle(frame, font, row, column) -> None:
    def switch_event():
        current_value = scale_value.get()
        scale_switch.configure(text=f"{current_value}")     # ui element, not the swapping itself


    label = ctk.CTkLabel(frame, text="Show temperature in:", font=font)
    label.grid(row=row, column=column, sticky='w', padx=5)

    scale_value = ctk.StringVar(value="Fahrenheit")
    scale_switch = ctk.CTkSwitch(frame, text=f"{scale_value.get()}", command=switch_event,
                                 variable=scale_value, onvalue="Celsius", offvalue="Fahrenheit",
                                 font=font,  fg_color="forest green", progress_color="forest green")

    scale_switch.grid(row=row+1, column=column, padx=5, pady=10, sticky='w')
    # todo update scale_value in settings config_write
    row_spacer(frame, font, row+2, column)


def time_scale_toggle(frame, font, row, column) -> None:
    def switch_event():
        current_value = time_value.get()
        time_switch.configure(text=f"{current_value}")

    label = ctk.CTkLabel(frame, text="Show time in:", font=font)
    label.grid(row=row, column=column, sticky='w', padx=225)

    time_value = ctk.StringVar(value="24 Hour")
    time_switch = ctk.CTkSwitch(frame, text=f"{time_value.get()}", command=switch_event, variable=time_value,
                                onvalue="AM/PM", offvalue="24 Hour", font=font,  fg_color="forest green",
                                progress_color="forest green")

    time_switch.grid(row=row+1, column=column, padx=225, pady=10, sticky='w')
    # todo update scale_value in settings config_write
    row_spacer(frame, font, row+2, column)


def key_entry(frame, font, row, column, key) -> None:
    label_text(frame, 'AQI API Key:', font, row, column)
    if key != '':
        api_key_entry = ctk.CTkEntry(frame, placeholder_text=f'{key}', width=370, font=font)
    else:
        api_key_entry = ctk.CTkEntry(frame, placeholder_text="No saved key", width=370, font=font)

    api_key_entry.grid(row=row+1, column=column, padx=5, pady=10, sticky='w')
    row_spacer(frame, font, row+2, column)
    # todo save value as key in settings config_write


def profile_select(frame, font, row, column) -> None:
    def combobox_callback(choice):
        return choice

    label_text(frame, "Profile:", font, row=row, column=column)

    combobox_var = ctk.StringVar(value="Default")
    profile_combobox = ctk.CTkComboBox(frame, values=["Morning", "Night", "Default", "Custom"],
                                       command=combobox_callback, variable=combobox_var, font=font)
    profile_combobox.set("Profile")

    profile_combobox.grid(row=row+1, column=column, padx=5, pady=10, sticky='w')

    #   if combobox_callback != "Custom":
    placeholder_text = "Enter custom profile name"
    entry = ctk.CTkEntry(frame, placeholder_text=placeholder_text, font=font,
                         width=150)
    entry.grid(row=row+1, column=column, padx=300, pady=10, sticky='w')
    # else:
    #    placeholder_text = "Enter custom profile name"
    #    entry = ctk.CTkEntry(frame, placeholder_text=placeholder_text, font=font, state='normal',
    #                         width=150)
    #    entry.grid(row=row+1, column=column, padx=300, pady=10, sticky='w')

    row_spacer(frame, font, row+2, column)


# todo save button that updates the settings
def save_settings(frame, font, row, column) -> None:
    def save_pushed():
        print("Save button pushed")

    save_button = ctk.CTkButton(frame, text="Save Changes", command=save_pushed, fg_color="forest green",
                                font=font, width=200)
    save_button.grid(row=row, column=column, sticky='nsw')
    row_spacer(frame, font, row + 1, column)


# todo save button that updates the settings
def cancel_settings(frame, font, row, column) -> None:
    def cancel_pushed():
        print("Cancel button pushed")


    cancel_button = ctk.CTkButton(frame, text="Cancel Changes", command=cancel_pushed, fg_color="red4",
                                font=font, width=200)
    cancel_button.grid(row=row, column=column, sticky='ns', padx=225)
    row_spacer(frame, font, row + 1, column)


# ------------------------


def aqi_button(frame, row, column, font):
    def callback():
        webbrowser.open_new("https://en.wikipedia.org/wiki/Air_quality_index#United_States")

    button = ctk.CTkButton(
        frame, text=f'Learn about the US AQI scale  \U0001F517', font=font, command=lambda: callback(),
        fg_color="forest green")
    button.grid(row=row, column=column, sticky='w', padx=5, pady=5)

# ----------------------------------------------------------------------------
# fixme this has the power to throw off all of the placement settings


def links_display(frame, font, row, column, response_dict) -> None:
    def callback(url):
        webbrowser.open_new(url)


    label_text(frame, text="API Sources and Attribution:\n", font=font, row=row, column=column)

    # attributions as required by weather report API
    row += 2
    for each in response_dict['data']['attributions']:
        # text = f"{each['name']}: {each['url']}\n"\U0001F517'
        button = ctk.CTkButton(frame, text={each['name']}, command=lambda url=each['url']: callback(url),
                               fg_color="forest green", font=font)
        
        button.grid(row=row, column=column, sticky='w', pady=5)
        row += 1
    row_spacer(frame, font, row + 1, column)

    # additional info
    label_text(frame, text="Additional Information:\n", font=font, row=row+2, column=column)
    aqi_button(frame, row + 3, column, font)

# ----------------------------------------------------------

"""
if __name__ == "__main__":
    root = ctk.CTk()
    frame = ctk.CTkFrame(root)
    frame.pack()

    # fixme need a getter/setter to fix the stuff sent to the two below?
    font = ('Helvetica', 16)
    temp_scale_toggle(frame, font, row=0, column=0)
    time_scale_toggle(frame, font, row=0, column=0)
    profile_select(frame, font, row=0, column=0)
    root.mainloop()
"""