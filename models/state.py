#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class State(BaseModel):
    """ State class """
    __tablename__ = "state"
    name = Column(String(128), nullable=False)
    cities = relationship('City' cascade='all , delete, delete=orphan',
                            back_populates='state')
