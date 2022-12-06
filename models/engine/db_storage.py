#!/usr/bin/python3
from models.base_model import BaseModel
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import mySQLdb
from os import getenv


user = getenv("HBNB_MYSQL_USER")
passwd = getenv("HBNB_MYSQL_PWD")
host = getenv("localhost")
db = getenv("HBNB_MYSQL_DB")

self.__engine = engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}\
        ".format(user, passwd, host, db, (pool_pre_ping=True)))
if getenv(HBNB_ENV) == "test":
    Base.metadata.drop_all(self.__engine)
