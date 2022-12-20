from ast import Str
from sqlalchemy import Table, Column, Integer, String, Date, Boolean, ForeignKey, MetaData, text
from sqlalchemy.orm import relationship, backref
from .database import Base, engine
from sqlalchemy.schema import CreateColumn
import datetime



Base.metadata.create_all(engine)    