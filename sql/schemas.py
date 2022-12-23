from pydantic import BaseModel
from . import models
from typing import List

class CountryBase(BaseModel):
    country_name: str
    year: int
    GDP: float
    GDP_growth: float
    GDP_pc: float
    inflation: float = None
    population: float
    surface: float
    imports: float
    exports: float 
    continent_id: int
    # continent = models.Continent


class ContinentBase(BaseModel):
    continent_name: str 
    # countries: List[CountryBase] = []


class RegionBase(BaseModel):
    region_name: str
