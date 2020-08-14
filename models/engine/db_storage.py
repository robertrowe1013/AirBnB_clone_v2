#!/usr/bin/python3
""" db storage """
from sqlalchemy import create_engine
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import os


class DBStorage():
    """ DBStorage class """
    __engine = None
    __session = None

    def __init__(self):
        """ init DBS """
        msuser = os.getenv('HBNB_MYSQL_USER')
        mspasswd = os.getenv('HBNB_MYSQL_PWD')
        mshost = os.getenv('HBNB_MYSQL_HOST')
        msdb = os.getenv('HBNB_MYSQL_DB')
        url = 'mysql+mysqldb://{}:{}@{}/{}'.format(msuser, mspasswd, mshost,
                                                   msdb)
        env = os.getenv('HBNB_ENV')
        self.__engine = create_engine(url, pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query all objects of cls """
        tmp = {}
        if cls is None:
            allobjs = self.__session.query(State).all()
            allobjs += self.__session.query(City).all()
            allobjs += self.__session.query(User).all()
            allobjs += self.__session.query(Place).all()
            allobjs += self.__session.query(Amenity).all()
            allobjs += self.__session.query(Review).all()
        else:
            allobjs = self.__session.query(cls).all()
        for obj in allobjs:
            key = obj.__class__.__name__ + '.' + obj.id
            tmp.update({key: obj})
        return tmp

    def new(self, obj):
        """ add obj to db """
        self.__session.add(obj)

    def save(self):
        """ commit changes to db """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete obj from db """
        if obj is not None:
            self.__session.query(obj).delete

    def reload(self):
        """ reload db """
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()
