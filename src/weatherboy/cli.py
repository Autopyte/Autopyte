#  Copyright (c) 2023 Autopyte - All Rights Reserved
#  This file is part of Project WeatherBoy and is released under the "MIT License Agreement"
#  Please see the LICENSE file that should have been included as part of this package

from datetime import datetime
from typing import Any

import questionary

from weatherboy.models import City
from weatherboy.service import search_for_cities, get_current_weather
from weatherboy.utils import get_or_default, create_table, reset_current_line, pprint, degrees_to_direction, get_weather_icon


def entrypoint() -> None:
    # Intro
    pprint("""
        __        __         _   _               ____              
        \ \      / /__  __ _| |_| |__   ___ _ __| __ )  ___  _   _ 
         \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__|  _ \ / _ \| | | |
          \ V  V /  __/ (_| | |_| | | |  __/ |  | |_) | (_) | |_| |
           \_/\_/ \___|\__,_|\__|_| |_|\___|_|  |____/ \___/ \__, |
                                                             |___/ 
    """)  # noqa

    # Search for City
    query: str = questionary.text("Enter the city name").ask()

    latitude: float = 0.0
    longitude: float = 0.0

    pprint("Searching Cities ...", style="fg:cyan", end='')

    cities: list[City] = search_for_cities(query)
    reset_current_line()

    if not cities:
        pprint()
        pprint("No such city found !!!", style="fg:red")
        return

    elif len(cities) == 1:
        latitude: float = cities[0].lat
        longitude: float = cities[0].lon

    else:
        selected_city_name: str = questionary.select(
            "Choose one", [city.display_name for city in cities]
        ).ask()

        for city in cities:
            if selected_city_name == city.display_name:
                latitude: float = city.lat
                longitude: float = city.lon
                break

    # Fetch current weather
    pprint("Fetching Weather Details ...", style="fg:cyan", end='')

    weather_data: Any = get_current_weather(latitude, longitude)
    reset_current_line()

    # pprint
    current_weather(weather_data)

    # Detailed weather
    if questionary.confirm("Do you want to view the detailed weather report").ask():
        detailed_weather(weather_data)
        current_details(weather_data)
        wind(weather_data)
        sunrise_and_sunset(weather_data)

    # End
    pprint()
    pprint("Thank You for using WeatherBoy", style="fg:cyan")


def current_weather(data: dict) -> None:
    pprint()
    pprint(f"Current Weather at {data['name']}")
    pprint()
    table_data = {
        'Weather': get_weather_icon(get_or_default(data, ['weather', 0, 'icon'])) + ' '
                   + get_or_default(data, ['weather', 0, 'main']),
        'Temperature': get_or_default(data, ['main', 'temp'], cast=float, unit_format="%.2f °C"),
        'Feels Like': get_or_default(data, ['main', 'feels_like'], cast=float, unit_format="%.2f °C"),
    }
    pprint(create_table(table_data))
    pprint()


def detailed_weather(data: dict) -> None:
    pprint()
    pprint(f"Detailed Weather at {data['name']}")
    pprint()
    table_data = {
        'Weather': get_or_default(data, ['weather', 0, 'main']),
        'Description': get_or_default(data, ['weather', 0, 'description']),
        'Temperature': get_or_default(data, ['main', 'temp'], cast=float, unit_format="%.2f °C"),
        'Feels Like': get_or_default(data, ['main', 'feels_like'], cast=float, unit_format="%.2f °C"),
        'Min Temp': get_or_default(data, ['main', 'temp_min'], cast=float, unit_format="%.2f °C"),
        'Max Temp': get_or_default(data, ['main', 'temp_max'], cast=float, unit_format="%.2f °C"),
    }
    pprint(create_table(table_data))
    pprint()


def current_details(data: dict) -> None:
    pprint()
    pprint(f"Current Details")
    pprint()
    table_data = {
        'Pressure': get_or_default(data, ['main', 'pressure'], cast=int, unit_format="%d hPa"),
        'Humidity': get_or_default(data, ['main', 'humidity'], cast=int, unit_format="%d %%"),
        'Sea Level': get_or_default(data, ['main', 'sea_level'], cast=int, unit_format="%d hPa"),
        'Ground Level': get_or_default(data, ['main', 'grnd_level'], cast=int, unit_format="%d hPa"),
        'Visibility': get_or_default(data, ['visibility'], cast=lambda m: float(m) / 1000, unit_format="%.2f km"),
    }
    pprint(create_table(table_data))
    pprint()


def wind(data: dict) -> None:
    pprint()
    pprint(f"Wind")
    pprint()
    table_data = {
        'Speed': get_or_default(data, ['wind', 'speed'], cast=float, unit_format="%.2f m/s"),
        'Degree / Direction': get_or_default(data, ['wind', 'deg'], cast=int, unit_format="%d°") + ' / '
                              + get_or_default(data, ['wind', 'deg'], cast=lambda x: degrees_to_direction(x)),
        'Gust': get_or_default(data, ['wind', 'gust'], cast=float, unit_format="%.2f m/s"),
    }
    pprint(create_table(table_data))
    pprint()


def sunrise_and_sunset(data: dict) -> None:
    pprint()
    pprint(f"Sunrise & Sunset")
    pprint()
    table_data = {
        'Sunrise': get_or_default(data, ['sys', 'sunrise'], cast=lambda t: datetime.fromtimestamp(t)),
        'Sunset': get_or_default(data, ['sys', 'sunset'], cast=lambda t: datetime.fromtimestamp(t)),
    }
    pprint(create_table(table_data))
    pprint()


if __name__ == '__main__':
    entrypoint()
