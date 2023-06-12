#  Copyright (c) 2023 Autopyte - All Rights Reserved
#  This file is part of Project WeatherBoy and is released under the "MIT License Agreement"
#  Please see the LICENSE file that should have been included as part of this package

from weatherboy.client import search_location, fetch_current_weather, fetch_weather_forecast


def test_search_location() -> None:
    response = search_location("London")
    assert response is not None
    assert type(response) is list


def test_fetch_current_weather() -> None:
    response = fetch_current_weather(17.360589, 78.4740613)
    assert response is not None


def test_fetch_weather_forecast() -> None:
    response = fetch_weather_forecast(17.360589, 78.4740613)
    assert response is not None
