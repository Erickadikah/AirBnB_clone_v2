#!/usr/bin/python3
from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import mySQLdb
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import create_engine


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

       # self.__engine = engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(user, passwd, host, db), pool_pre_ping=True)
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, database, pool_pre_ping=True))

    if env == "test":
        Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls is None:
            objs = self.__session.query(User).all()
            objs.extend(self.__session.query(State).all())
            objs.extend(self.__session.query(City).all())
            objs.extent(self.__session.query(Amenity).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())

        else:
             if type(cls) == str:
                cls = eval(cls)
                obj = self.__session.query(cls)

        return {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in objs}

    def new(self, obj):
        self.session.add(obj)
    """a funtion to add current database session"""

    def save(self):
        self.session.commit()
    """a function to save"""

    def delete(self, obj=none):
        if obj is not None:
            self.session.delete(obj)
    """a function to delete current database session"""

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session.factory = session.maker(bind=self.__engine,
                                    expire_on_commit=False)
        session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        self.__session.close()
