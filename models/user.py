#!/usr/bin/python3
"""module for user class, inherits from the Base and BaseModel classes"""
from models.base_mode import BaseModel, Base
from sqlalchemy import String, Column


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
