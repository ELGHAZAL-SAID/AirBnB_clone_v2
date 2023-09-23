#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ

class State(BaseModel, Base):
    """ State class """
    __tabename__ = 'states'
    name = Column(String(128), nullable=False)

    if environ['HBNB_TYPE_STORAGE'] == 'db':
        cities = relationship('City',cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            """Getter Method"""
            from models import storage
            from models.city import City
            cities_dict = storage.all(City)
            cities_list = []
            for city in cities_dict.values():
                if city.state_id == slef.id:
                    cities_list.append(city)
            return cities_list
