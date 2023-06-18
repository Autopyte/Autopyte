#  Copyright (c) 2023 Autopyte - All Rights Reserved
#  This file is part of Project WeatherBoy and is released under the "MIT License Agreement"
#  Please see the LICENSE file that should have been included as part of this package

from pydantic import BaseModel


class City(BaseModel):
    name: str
    state: str = ""
    country: str = ""
    lat: float
    lon: float

    @property
    def display_name(self):
        res = self.name
        if self.state:
            res += ', ' + self.state
        if self.country:
            res += ', ' + self.country
        return res
