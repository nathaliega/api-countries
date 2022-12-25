from ast import Str
from sqlalchemy import Table, Column, Float, String, Date, Boolean, ForeignKey, MetaData, text, Integer
from sqlalchemy.orm import relationship, backref
from .database import Base, engine
from sqlalchemy.schema import CreateColumn
import datetime

class Country(Base):
    __tablename__ = "countries"

    country_id = Column(Integer, primary_key = True)
    country_name = Column(String)
    year = Column(Integer)
    GDP = Column(Float, nullable=True)
    GDP_growth = Column(Float, nullable=True)
    GDP_pc = Column(Float, nullable=True)
    inflation = Column(Float, nullable=True)
    population = Column(Float)
    surface = Column(Float, nullable=True)
    imports = Column(Float, nullable=True)
    exports = Column(Float, nullable=True)
    continent_id = Column(Integer, ForeignKey('continents.continent_id'))
    region_id = Column(Integer, ForeignKey('regions.region_id'))

    continent = relationship('Continent', back_populates='countries')
    region = relationship('Region', back_populates='countries')


class Continent(Base):
    __tablename__ = 'continents'

    continent_id = Column(Integer, primary_key = True)
    continent_name = Column(String, unique=True)

    countries = relationship('Country', back_populates = 'continent')


class Region(Base):
    __tablename__ = 'regions'

    region_id = Column(Integer, primary_key = True)
    region_name = Column(String, unique=True)

    countries = relationship('Country', back_populates='region')

Base.metadata.create_all(engine)    