#  Copyright (c) 2023 Autopyte - All Rights Reserved
#  This file is part of Project WeatherBoy and is released under the "MIT License Agreement"
#  Please see the LICENSE file that should have been included as part of this package

import sys
from typing import Any, Callable

import questionary
from tabulate import tabulate


def get_or_default(data: dict, key: list, default: str = '-', cast: Callable = str, unit_format: str = "%s") -> str:
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
    return tabulate([[k, ':', v] for k, v in table_data.items()], tablefmt='plain')


def pprint(text: str = '', style: str = None, **kwargs: Any) -> None:
    questionary.print(text, style, **kwargs)


def reset_current_line() -> None:
    max_cols: int = 100
    sys.stdout.write("\r{}\r".format(' ' * max_cols))
    sys.stdout.flush()


def degrees_to_direction(degrees: str | int) -> str:
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
