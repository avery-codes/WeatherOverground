import customtkinter as ctk


# Checkbox buttons
def tb_settings(settings, hour) -> bool:
    start = settings.start_time[:1]
    end = settings.end_time[:1]
    if hour >= start:
        if hour <= end:
            checked = True
            return checked
        else:
            checked = False
            return checked


def checkbox_event() -> bool:
    return True


def tb_list(hour) -> str:   # fixme where the hell do I get hour from??
    checkbox_num = f"{hour}:00"
    return checkbox_num