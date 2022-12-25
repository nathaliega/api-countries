from sqlalchemy import or_
from sqlalchemy.orm import Session
from . import models, schemas,database


class NotFoundException(Exception):
    pass

def get_country_by_name(country_name: str, db: Session):
    rows = db.query(models.Country).filter(models.Country.country_name == country_name).all()
    
    if not rows:
        raise NotFoundException
    
    my_dict = {}
    for row in rows:
        my_dict[str(row.year)] = row
    final_dict = {
        "country_name": country_name,
        "continent": rows[0].continent,
        "region": rows[0].region,
        "years": my_dict
    }
    return final_dict

def get_continent(continent_name: str, db: Session):
    countries = db.query(models.Country).join(models.Continent).filter(models.Continent.continent_name == continent_name,
                models.Country.year == 1998).all()
    if not countries:
        raise NotFoundException
    
    my_dict = {}
    for country in countries:
        my_dict[country.country_name] = country
    final_dict = {
        "continent_name": continent_name,
        "countries": my_dict
    }
    return final_dict

def add_country(country: schemas.CountryBase):
    db_session = database.SessionLocal()

    country = models.Country(**country.dict())
    db_session.add(country)
    db_session.commit()
    db_session.close()

def add_region(region: schemas.RegionBase):
    db_session = database.SessionLocal()

    region = models.Region(**region.dict())
    db_session.add(region)
    db_session.commit()
    db_session.close()

def get_continent_by_name(continent: str):
    db_session = database.SessionLocal()

    continent = db_session.query(models.Continent).filter(models.Continent.continent_name == continent).first()
    db_session.close()
    return continent

def get_region_by_name(region: str):
    db_session = database.SessionLocal()

    region = db_session.query(models.Region).filter(models.Region.region_name == region).first()
    db_session.close()
    return region

def add_continent(continent: schemas.ContinentBase):
    db_session = database.SessionLocal()

    continent = models.Continent(**continent.dict())
    db_session.add(continent)
    db_session.commit()
    db_session.close()

# def add_region(region: schemas.ContinentBase):
#     db_session = database.SessionLocal()

#     continent = models.Continent(**continent.dict())
#     db_session.add(continent)
#     db_session.commit()
#     db_session.close()