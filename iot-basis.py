from sqlalchemy import Column, Integer, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy_utils.functions import drop_database, create_database,\
  database_exists

Basis = declarative_base()
class Meting(Basis):
  __tablename__ = 'metingen'
  id = Column(Integer, primary_key=True)
  tijdstempel = Column(DateTime, nullable=False)
  meetwaarde = Column(Float, nullable=False)

engine = create_engine("mysql://dbroot:$ecret1@localhost/iot_metingen")
#if database_exists(engine.url):
#  drop_database(engine.url)
if not database_exists(engine.url):
  create_database(engine.url)

Basis.metadata.create_all(engine)
