#  Copyright (c) 2023 Autopyte - All Rights Reserved
#  This file is part of Project WeatherBoy and is released under the "MIT License Agreement"
#  Please see the LICENSE file that should have been included as part of this package

from pydantic import BaseModel


class City(BaseModel):
    name: str
    state: str
    country: str
    lat: float
    lon: float
