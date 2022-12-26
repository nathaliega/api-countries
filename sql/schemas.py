from pydantic import BaseModel
from . import models
from typing import List, Dict

class Error(BaseModel):
    message: str

class CountryBase(BaseModel):
    class Config:
        orm_mode = True

class CountryCreate(CountryBase):
    country_name: str =None
    year: int =None
    GDP: float = None
    GDP_growth: float = None
    GDP_pc: float = None
    inflation: float = None
    population: float = None
    surface: float = None
    imports: float = None
    exports: float = None
    continent_name: str = None
    region_name: str = None
    # continent = models.Continent

class ContinentBase(BaseModel):
    continent_name: str 
    class Config:  
        orm_mode = True

class RegionBase(BaseModel):
    region_name: str
    class Config:
        orm_mode = True

class CountryByYear(CountryBase):
    GDP: float = None
    GDP_growth: float = None
    GDP_pc: float = None
    inflation: float = None
    population: float = None
    surface: float = None
    imports: float = None
    exports: float = None

class ReturnCountry(CountryBase):
    country_name: str =None
    continent: ContinentBase = None
    region: RegionBase = None
    years: Dict[str, CountryByYear] = None

class ShortCountry(CountryBase):
    population: float = None
    surface: float = None

class LongCountry(CountryBase):
    country_name: str =None
    year: int =None
    GDP: float = None
    GDP_growth: float = None
    GDP_pc: float = None
    inflation: float = None
    population: float = None
    surface: float = None
    imports: float = None
    exports: float = None
    continent: ContinentBase = None
    region: RegionBase = None
    

class ReturnContinent(ContinentBase):
    countries: Dict[str, ShortCountry] = None


class ReturnRegion(RegionBase):
    countries: Dict[str, ShortCountry] = None



