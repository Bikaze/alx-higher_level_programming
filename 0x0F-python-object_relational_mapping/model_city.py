#!/usr/bin/python3
"""This file contains the definition of the City model"""
from model_state import Base
from sqlalchemy import Integer, Column, String, ForeignKey


class City(Base):
    """This class (City) is a model for the table cities"""
    __tablename__ = 'cities'
    id = Column(Integer(), primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)
