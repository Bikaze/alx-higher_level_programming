from sqlalchemy import Table, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
"""This code creates the class 'State'"""
Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
