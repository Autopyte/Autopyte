#  Copyright (c) 2023 Autopyte - All Rights Reserved
#  This file is part of Project WeatherBoy and is released under the "MIT License Agreement"
#  Please see the LICENSE file that should have been included as part of this package

from typing import Any, List
from client import search_location, fetch_current_weather
from weatherboy.models import City


def search_for_cities(query: str) -> list[City]:
    city_list_json = search_location(query)
    city_list: list[City] = []
    for city in city_list_json:
        city_list.append(City(city["name"], city["state"], city["country"], city["lat"], city["lon"]))
    return city_list


def get_current_weather(latitude: float, longitude: float) -> Any:
    return fetch_current_weather(latitude, longitude)
