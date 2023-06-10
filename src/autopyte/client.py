#  Copyright (c) 2023 Autopyte - All Rights Reserved
#  This file is part of the Autopyte App and is released under the "MIT License Agreement"
#  Please see the LICENSE file that should have been included as part of this package

from typing import Any

import requests
from requests import Response

BASE_URL: str = "https://api.openweathermap.org"
API_KEY: str = "b1b15e88fa797225412429c1c50c122a1"

WEATHER_ENDPOINT: str = "/data/3.0/onecall"
GEO_ENDPOINT: str = "/geo/1.0/direct"


def search_location(q: str) -> Any:
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

