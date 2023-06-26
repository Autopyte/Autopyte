#  Copyright (c) 2023 Autopyte - All Rights Reserved
#  This file is part of Project WeatherBoy and is released under the "MIT License Agreement"
#  Please see the LICENSE file that should have been included as part of this package

import sys
from typing import Any, Callable

import questionary
from tabulate import tabulate


def get_or_default(data: dict, key: list, default: str = '-', cast: Callable = str, unit_format: str = "%s") -> str:
    """
    Retrieves value using key from the given data and formats it.

    :param data: complete JSON data as dictionary
    :param key: key to find (e.g. ['weather', 0, 'main'])
    :param default: (Optional) default value if key not found
    :param cast: (Optional) data type of the value
    :param unit_format: (Optional) representation format for given unit of data
    :return: The value associated with the key
    """
    try:
        val = data
        for k in key:
            val = val[k]
        return unit_format % cast(val)
    except KeyError:
        if default == '-':
            return default
        return unit_format % cast(default)


def create_table(table_data: dict[str, str]) -> str:
    """
    Converts key-value pair of data into tabular notation.

    :param table_data: data as key-value pairs
    :return: the data in tabular format
    """
    return tabulate([[k, ':', v] for k, v in table_data.items()], tablefmt='plain')


def pprint(text: str = '', style: str = None, **kwargs: Any) -> None:
    """
    Alternative to the default print() with support for styling of text.

    :param text: The text to print
    :param style: (Optional) The style information for the text to print (e.g. 'fg:cyan')
    :param kwargs: (Optional) Additional parameters
    """
    questionary.print(text, style, **kwargs)


def reset_current_line() -> None:
    """
    Clears the current line in the terminal. It is assumed that the current line is maximum 100 characters long.
    """
    max_cols: int = 100
    sys.stdout.write("\r{}\r".format(' ' * max_cols))
    sys.stdout.flush()


def degrees_to_direction(degrees: str | int) -> str:
    """
    Converts wind direction in degrees notation to suitable labels.

    :param degrees: wind direction in degrees
    :return: label of wind direction (e.g. North-East)
    """
    if isinstance(degrees, str):
        degrees = int(degrees)

    if (337.5 <= degrees <= 360) or (0 <= degrees < 22.5):
        return 'North'
    elif 22.5 <= degrees < 67.5:
        return 'North-East'
    elif 67.5 <= degrees < 112.5:
        return 'East'
    elif 112.5 <= degrees < 157.5:
        return 'South-East'
    elif 157.5 <= degrees < 202.5:
        return 'South'
    elif 202.5 <= degrees < 247.5:
        return 'South-West'
    elif 247.5 <= degrees < 292.5:
        return 'West'
    elif 292.5 <= degrees < 337.5:
        return 'North-West'
    else:
        return 'Unknown'


WEATHER_ICONS = {
    '01d': '☀️',
    '01n': '🌙',
    '02d': '⛅',
    '02n': '⛅',
    '03d': '☁️',
    '03n': '☁️',
    '04d': '☁️',
    '04n': '☁️',
    '09d': '🌧️',
    '09n': '🌧️',
    '10d': '🌦️',
    '10n': '🌦️',
    '11d': '⛈️',
    '11n': '⛈️',
    '13d': '❄️',
    '13n': '❄️',
    '50d': '🌫️',
    '50n': '🌫️'
}


def get_weather_icon(icon: str) -> str:
    """
    Converts weather icon to suitable emoji.

    :param icon: weather icon
    :return: emoji for weather icon
    """
    return WEATHER_ICONS.get(icon, '❓')
