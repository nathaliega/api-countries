from pydantic import BaseModel
from . import models
from typing import List, Dict

class Error(BaseModel):
    message: str

class CountryBase(BaseModel):
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
    continent_id: int = None
    region_id: int = None
    # continent = models.Continent
    class Config:
        orm_mode = True

class ContinentBase(BaseModel):
    continent_name: str 
    # countries: List[CountryBase] = []
    class Config:  
        orm_mode = True

class CountryByYear(BaseModel):
    GDP: float = None
    GDP_growth: float = None
    GDP_pc: float = None
    inflation: float = None
    population: float = None
    surface: float = None
    imports: float = None
    exports: float = None
    
    class Config:
        orm_mode = True

class RegionBase(BaseModel):
    region_name: str

    class Config:
        orm_mode = True

class ReturnCountry(BaseModel):
    country_name: str =None
    continent: ContinentBase = None
    region: RegionBase = None
    years: Dict[str, CountryByYear] = None

    class Config:
        orm_mode = True


class ShortCountry(BaseModel):
    population: float = None
    surface: float = None

    class Config:
        orm_mode = True

class ReturnContinent(BaseModel):
    continent_name: str =None
    countries: Dict[str, ShortCountry] = None

    class Config:
        orm_mode = True





