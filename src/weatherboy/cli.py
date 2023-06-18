#  Copyright (c) 2023 Autopyte - All Rights Reserved
#  This file is part of Project WeatherBoy and is released under the "MIT License Agreement"
#  Please see the LICENSE file that should have been included as part of this package

from typing import Any

import questionary

from weatherboy.models import City
from weatherboy.service import search_for_cities, get_current_weather
from weatherboy.utils import get_or_default, create_table


def entrypoint() -> None:
    # Intro
    print("""
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

    cities: list[City] = search_for_cities(query)
    if not cities:
        print("No such city found !!!")
        return

    elif len(cities) == 1:
        latitude: float = cities[0].lat
        longitude: float = cities[0].lon

    else:
        selected_city_name: str = questionary.select(
            "Choose one", [f"{city.name}, {city.state}, {city.country}" for city in cities]
        ).ask()

        for city in cities:
            if f"{city.name}, {city.state}, {city.country}" == selected_city_name:
                latitude: float = city.lat
                longitude: float = city.lon
                break

    # Fetch current weather
    weather_data: Any = get_current_weather(latitude, longitude)

    # Print
    current_weather(weather_data)

    # Detailed weather
    if questionary.confirm("Do you want to view the detailed weather report").ask():
        detailed_weather(weather_data)
        current_details(weather_data)
        wind(weather_data)
        sunrise_and_sunset(weather_data)

    # End
    print("Thank You for using WeatherBoy")


def current_weather(data: dict) -> None:
    print()
    print(f"Current Weather at {data['name']}")
    print()
    table_data = {
        'Weather': get_or_default(data, ['weather', 0, 'main']),
        'Temperature': get_or_default(data, ['main', 'temp']),
        'Feels Like': get_or_default(data, ['main', 'feels_like']),
    }
    print(create_table(table_data))
    print()


def detailed_weather(data: dict) -> None:
    print()
    print(f"Detailed Weather at {data['name']}")
    print()
    table_data = {
        'Weather': get_or_default(data, ['weather', 0, 'main']),
        'Description': get_or_default(data, ['weather', 0, 'description']),
        'Temperature': get_or_default(data, ['main', 'temp']),
        'Feels Like': get_or_default(data, ['main', 'feels_like']),
        'Min Temp': get_or_default(data, ['main', 'temp_min']),
        'Max Temp': get_or_default(data, ['main', 'temp_max']),
    }
    print(create_table(table_data))
    print()


def current_details(data: dict) -> None:
    print()
    print(f"Current Details")
    print()
    table_data = {
        'Pressure': get_or_default(data, ['main', 'pressure']),
        'Humidity': get_or_default(data, ['main', 'humidity']),
        'Sea Level': get_or_default(data, ['main', 'sea_level']),
        'Ground Level': get_or_default(data, ['main', 'grnd_level']),
        'Visibility': get_or_default(data, ['visibility']),
    }
    print(create_table(table_data))
    print()


def wind(data: dict) -> None:
    print()
    print(f"Wind")
    print()
    table_data = {
        'Speed': get_or_default(data, ['wind', 'speed']),
        'Degree / Direction': get_or_default(data, ['wind', 'deg']),
        'Gust': get_or_default(data, ['wind', 'gust']),
    }
    print(create_table(table_data))
    print()


def sunrise_and_sunset(data: dict) -> None:
    print()
    print(f"Sunrise & Sunset")
    print()
    table_data = {
        'Sunrise': get_or_default(data, ['sys', 'sunrise']),
        'Sunset': get_or_default(data, ['sys', 'sunset']),
    }
    print(create_table(table_data))
    print()
