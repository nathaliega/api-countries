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
    GDP = Column(Float)
    GDP_growth = Column(Float)
    GDP_pc = Column(Float)
    inflation = Column(Float, nullable=True)
    population = Column(Float)
    surface = Column(Float)
    imports = Column(Float)
    exports = Column(Float)
    continent_id = Column(Integer, ForeignKey('continents.continent_id'))

    continent = relationship('Continent', back_populates='countries')

    # reginon_id = relationship('Continents')



class Continent(Base):
    __tablename__ = 'continents'

    continent_id = Column(Integer, primary_key = True)
    continent_name = Column(String, unique=True)

    countries = relationship('Country', back_populates = 'continent')


# class Regions(Base):
#     __tablename__ = 'regions'

#     reginon_id = Column(Float, primary_key = True)
#     regimonn_name = Column(String)

Base.metadata.create_all(engine)    