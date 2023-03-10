# from sqlalchemy import or_
from sqlalchemy.orm import Session
from . import models, schemas, database
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation


class NotFoundException(Exception):
    pass

# region country


def get_country_by_name(country_name: str, db: Session):
    rows = db.query(models.Country).filter(models.Country.country_name ==
                                           country_name).all()

    if not rows:
        raise NotFoundException

    return rows


def add_country(country: schemas.CountryCreate, db: Session):
    try:
        dict = country.dict()
        continent_name = dict['continent_name']
        region_name = dict['region_name']
        del dict['continent_name']
        del dict['region_name']
        new_country = models.Country(**dict,
                                     continent=get_continent_by_name(continent_name, db),
                                     region=get_region_by_name(region_name, db))
        db.add(new_country)
        db.commit()
    except IntegrityError:
        pass
    except UniqueViolation:
        print(f"{country} already exists")

    return new_country


def country_by_year(country: str, year: int, db: Session):
    country = db.query(models.Country).filter(models.Country.country_name ==
                                              country.capitalize(), models.Country.year ==
                                              year).first()
    if not country:
        raise NotFoundException

    return country

# endregion country

# region continent


def get_countries_from_continent(continent_name: str, db: Session):
    countries = db.query(models.Country).join(models.Continent).filter(
        models.Continent.continent_name == continent_name,
        models.Country.year == 1998).all()
    if not countries:
        raise NotFoundException

    return countries


def get_continent_by_name(continent: str, db: Session):
    db_session = database.SessionLocal()

    continent = db_session.query(models.Continent).filter(
        models.Continent.continent_name == continent).first()
    db_session.close()
    return continent


def add_continent(continent: schemas.ContinentBase, db: Session):
    # dict = continent.dict()
    try:
        new_continent = models.Continent(**continent.dict())
        db.add(new_continent)
        db.commit()
    except IntegrityError:
        pass
    except UniqueViolation:
        print(f"{continent} already exists")

    return new_continent

# endregion continent

# region region


def get_region_by_name(region: str, db: Session):
    db_session = database.SessionLocal()

    region = db_session.query(models.Region).filter(
        models.Region.region_name == region).first()
    db_session.close()
    return region


def get_countries_from_region(region_name: str, db: Session):
    countries = db.query(models.Country).join(models.Region).filter(
        models.Region.region_name == region_name,
        models.Country.year == 1998).all()
    if not countries:
        raise NotFoundException

    return countries


def add_region(region: schemas.RegionBase, db: Session):
    try:
        new_region = models.Region(**region.dict())
        db.add(new_region)
        db.commit()
    except IntegrityError:
        pass
    except UniqueViolation:
        print(f"{region} already exists")

    return new_region

# endregion region
