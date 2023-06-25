#  Copyright (c) 2023 Autopyte - All Rights Reserved
#  This file is part of Project WeatherBoy and is released under the "MIT License Agreement"
#  Please see the LICENSE file that should have been included as part of this package

from typing import Any

import requests
from requests import Response

BASE_URL: str = "https://api.openweathermap.org"
API_KEY: str = "54c4b31043220bf31b4fd51fb22852ab"
UNITS: str = "metric"

CURRENT_WEATHER_ENDPOINT: str = "/data/2.5/weather"
FORECAST_ENDPOINT: str = "/data/2.5/forecast"
GEO_ENDPOINT: str = "/geo/1.0/direct"


def search_location(q: str, limit: int = 5) -> list:
    """
    Search for a location using the OpenWeatherMap API

    :param q: The location to search for (e.g. "London")
    :param limit: max number of cities to show
    :return: The response from the API
    """

    url: str = BASE_URL + GEO_ENDPOINT
    params: dict = {
        "q": q,
        "limit": limit,
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

    url: str = BASE_URL + CURRENT_WEATHER_ENDPOINT
    params: dict = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": UNITS,
    }

    response: Response = requests.get(url, params=params)

    if response.status_code == 200:
        # return body as json
        return response.json()
    else:
        # raise error
        raise Exception("Unable to fetch weather data")


def fetch_weather_forecast(lat: float, lon: float) -> Any:
    """
    Fetch the weather forcast for a location using the OpenWeatherMap API

    :param lat: The latitude of the location
    :param lon: The longitude of the location
    :return: The response from the API i.e., 5 day / 3 hour forecast data
    """

    url: str = BASE_URL + CURRENT_WEATHER_ENDPOINT
    params: dict = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": UNITS,
    }

    response: Response = requests.get(url, params=params)

    if response.status_code == 200:
        # return body as json
        return response.json()
    else:
        # raise error
        raise Exception("Unable to fetch weather forecast")
