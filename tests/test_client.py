#  Copyright (c) 2023 Autopyte - All Rights Reserved
#  This file is part of Project WeatherBoy and is released under the "MIT License Agreement"
#  Please see the LICENSE file that should have been included as part of this package

from weatherboy.client import search_location


def test_search_location() -> None:
    response = search_location("London")
    assert response is not None
