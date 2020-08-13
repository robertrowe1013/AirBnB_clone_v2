#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if environ['HBNB_TYPE_STORAGE'] == 'db':
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            """ Returns a list of cities related to self """
            from models import storage
            from models.city import City
            citylist = storage.all(City)
            related = []

            for key in citylist.keys():
                if citylist[key].state_id == self.id:
                    related.append(citylist[key])

            return related
