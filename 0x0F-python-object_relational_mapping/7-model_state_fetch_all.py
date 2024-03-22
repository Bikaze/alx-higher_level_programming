#!/usr/bin/python3
"""Fetching all objects from the database
"""
import sys
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from urllib.parse import quote_plus

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], quote_plus(sys.argv[2]),
                                   sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State):
        print(f"{state.id}: {state.name}")
