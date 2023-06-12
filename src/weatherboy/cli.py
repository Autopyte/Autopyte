#  Copyright (c) 2023 Autopyte - All Rights Reserved
#  This file is part of Project WeatherBoy and is released under the "MIT License Agreement"
#  Please see the LICENSE file that should have been included as part of this package
from typing import Any

import questionary

from weatherboy.models import City
from weatherboy.service import search_for_cities, get_current_weather


def entrypoint() -> None:
    query: str = questionary.text("Enter the city name").ask()

    cities: list[City] = search_for_cities(query)
    selected_city_name: str = questionary.select(
        "Choose one", [f"{city.name}, {city.state}, {city.country}" for city in cities]
    ).ask()

    for city in cities:
        if f"{city.name}, {city.state}, {city.country}" == selected_city_name:
            latitude: float = city.lat
            longitude: float = city.lon
            break

    weather: Any = get_current_weather(latitude, longitude)
    print(weather)
