def make_sorting_data():
    sorting_data = [
        ["Time, ascending", "start time", "false"],     # fixme double sorting?
        ["Weight, descending", "weight", "true"],
        ["Time, descending", "start time", "true"],     # fixme double sorting?
        ["Temperature, ascending", "temperature", "false"],
        ["Temperature, descending", "temperature", "true"],
        ["Humidity, ascending", "humidity", "false"],
        ["Humidity, descending", "humidity", "true"],
        ["Rain Chance, ascending", "rain chance", "false"],
        ["Rain Chance, descending", "rain chance", "true"],
        ["Weight, ascending", "weight", "true"]
    ]
    return sorting_data


def get_sorting_values():
    sorting_data = make_sorting_data()
    sorting_values = []
    count = 0

    while count < len(sorting_data):
        name = str(sorting_data[count][0])
        count += 1
        sorting_values.append(name)

    return sorting_values



def sort_forecasts(forecast_list, attribute, reverse_direction):
    sorted_list = []

    first_list = sorted(forecast_list[0], key=lambda x: getattr(x, f'{attribute}'),
                        reverse=reverse_direction)

    second_list = sorted(forecast_list[1], key=lambda x: getattr(x, f'{attribute}'),
                         reverse=reverse_direction)

    third_list = sorted(forecast_list[2], key=lambda x: getattr(x, f'{attribute}'),
                        reverse=reverse_direction)

    sorted_list.append(first_list)
    sorted_list.append(second_list)
    sorted_list.append(third_list)

    return sorted_list