#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """epresents a review for a MySQL database.
    Inherits from SQLAlchemy Base and links to the MySQL table reviews.
    Attributes:
        __tablename__ (str): The name of the MySQL table to store Reviews.
        text (sqlalchemy String): The review description.
        place_id (sqlalchemy String): The review's place id.
        user_id (sqlalchemy String): The review's user id.
    """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("places.id"), nullable=None)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=None)
    text = Column(String(1024), nullable=None)
