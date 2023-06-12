#  Copyright (c) 2023 Autopyte - All Rights Reserved
#  This file is part of Project WeatherBoy and is released under the "MIT License Agreement"
#  Please see the LICENSE file that should have been included as part of this package

from typing import Any
from client import search_location, fetch_current_weather
from weatherboy.models import City


def search_for_cities(query: str) -> list[City]:
    return search_location(query)


def get_current_weather(latitude: float, longitude: float) -> Any:
    return fetch_current_weather(latitude, longitude)
