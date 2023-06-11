#  Copyright (c) 2023 Autopyte - All Rights Reserved
#  This file is part of Project WeatherBoy and is released under the "MIT License Agreement"
#  Please see the LICENSE file that should have been included as part of this package

from typing import Any

import requests
from requests import Response

BASE_URL: str = "https://api.openweathermap.org"
API_KEY: str = "54c4b31043220bf31b4fd51fb22852ab"

WEATHER_ENDPOINT: str = "/data/3.0/onecall"
GEO_ENDPOINT: str = "/geo/1.0/direct"


def search_location(q: str) -> list:
    """
    Search for a location using the OpenWeatherMap API

    :param q: The location to search for (e.g. "London")
    :return: The response from the API
    """

    url: str = BASE_URL + GEO_ENDPOINT
    params: dict = {
        "q": q,
        "limit": 5,
        "appid": API_KEY
    }

    response: Response = requests.get(url, params=params)

    if response.status_code == 200:
        # return body as json
        return response.json()
    else:
        # raise error
        raise Exception("Unable to find location")


def fetch_current_weather(lat: float, lon: float) -> Any:
    """
    Fetch the current weather for a location using the OpenWeatherMap API

    :param lat: The latitude of the location
    :param lon: The longitude of the location
    :return: The response from the API
    """

    url: str = BASE_URL + WEATHER_ENDPOINT
    params: dict = {
        "lat": lat,
        "lon": lon,
        "exclude": "minutely,hourly,daily",
        "appid": API_KEY
    }

    response: Response = requests.get(url, params=params)

    if response.status_code == 200:
        # return body as json
        return response.json()
    else:
        # raise error
        raise Exception("Unable to fetch weather data")
