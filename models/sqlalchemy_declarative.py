import os 
import sys
import datetime

from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()

class Price(Base):
    __tablename__ = 'Price'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    unit = Column(String, nullable=False)
    time = Column(DateTime, nullable=False)
    store = Column(String, nullable=False)
    location = Column(String)    # local
    url = Column(String)    # online

    def __repr__(self):
        return ("<Price(id={}, name={}, price={}, unit={}, record_time={})>"
               .format(self.id, self.name, self.price, self.unit, self.time))
