#!/usr/bin/python3
"""This file defines the State model"""

from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State model class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
