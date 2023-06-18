#  Copyright (c) 2023 Autopyte - All Rights Reserved
#  This file is part of Project WeatherBoy and is released under the "MIT License Agreement"
#  Please see the LICENSE file that should have been included as part of this package

from typing import Any

import questionary
from tabulate import tabulate


def get_or_default(data: dict, key: list, default: str = '-') -> str:
    try:
        val = data
        for k in key:
            val = val[k]
        return str(val)
    except KeyError:
        return str(default)


def create_table(table_data: dict[str, str]) -> str:
    return tabulate([[k, ':', v] for k, v in table_data.items()], tablefmt='plain')


def pprint(text: str = '', style: str = None, **kwargs: Any) -> None:
    questionary.print(text, style, **kwargs)


def reset_current_line() -> None:
    print("\r", end='')
