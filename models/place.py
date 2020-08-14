#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
import os

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)
        reviews = relationship("Review", cascade="all, delete",
                               backref="place")
    else:
        @property
        def reviews(self):
            """ Returns a list of reviews related to self """
            from models import storage
            from models.review import Review
            reviewlist = storage.all(Review)
            related = []

            for key in reviewlist.keys():
                if reviewlist[key].place_id == self.id:
                    related.append(reviewlist[key])

            return related

        @property
        def amenities(self):
            """ Represents all related amenities. """
            from models.amenity import Amenity
            from models import storage
            amens = storage.all(Amenity)
            related = []
            for key in amens.keys():
                if amens[key].id in amenity_ids:
                    related.append(amens[key])
            return related

        @amenities.setter
        def amenities(self, obj):
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                amenity_ids.append(obj.id)
