#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.amenity import Amenity
from models import storage
from sqlalchemy import Table, Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os

place_amenity = Table('place_amenity', Base.metadata, Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False), Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))


class Place(BaseModel):
    """ A place to stay """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)
    else:
        @property
        def amenities(self):
            """ Represents all related amenities. """
            amens = storage.all(Amenity)
            related = []
            for key in amens.keys():
                if amens[key].id in amenity_ids:
                    related.append(amens[key])
            return related

        @amenities.setter
        def amenities(self, obj):
            if isinstance(obj, Amenity):
                amenity_ids.append(obj.id)
