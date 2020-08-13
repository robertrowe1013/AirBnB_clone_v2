#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullabe=False)
    number_bathrooms = Column(Integer, default=0, nullabe=False)
    max_guest = Column(Integer, default=0, nullabe=False)
    price_by_night = Column(Integer, default=0, nullabe=False)
    latitude = Column(Float, nullabe=True)
    longitude = Column(Float, nullabe=True)
    amenity_ids = []
