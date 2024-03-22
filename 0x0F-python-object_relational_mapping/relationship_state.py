#!/usr/bin/python3
"""This file defines the State model"""

from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """State model class"""
    __tablename__ = 'states'
    id = Column(Integer(), primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
