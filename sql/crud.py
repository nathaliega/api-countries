from sqlalchemy import or_
from sqlalchemy.orm import Session
from . import models, schemas,database



def test():
    db_session = database.SessionLocal()

    country_1 = models.Country(country_name = 'Chile', continent = 
        db_session.query(models.Continent).filter(models.Continent.continent_name == "America")[0])

    db_session.add(country_1)
    db_session.commit()

    db_session.close()
    print("a")


def test_cont():
    db_session = database.SessionLocal()

    continent_1 = models.Continent(continent_name = 'America')

    db_session.add(continent_1)
    db_session.commit()
    db_session.close()


def get_country_by_name(country_name: str):
    db_session = database.SessionLocal()
    country = db_session.query(models.Country).filter(models.Country.country_name == country_name).first()
    db_session.close()
    return country


def add_country(country: schemas.CountryBase):
    db_session = database.SessionLocal()

    country = models.Country(**country.dict())
    db_session.add(country)
    db_session.commit()
    db_session.close()

def get_continent_by_name(continent: str):
    db_session = database.SessionLocal()

    continent = db_session.query(models.Continent).filter(models.Continent.continent_name == continent).first()
    db_session.close()
    return continent

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