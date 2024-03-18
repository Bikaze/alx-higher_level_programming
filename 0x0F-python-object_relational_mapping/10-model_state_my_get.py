#!/usr/bin/python3
"""Fetching only the first object from the database
"""
import sys
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from urllib.parse import quote_plus

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   quote_plus(sys.argv[2]), sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name ==
                                        (sys.argv[4], )).one_or_none()
    if state:
        print(state.id)
    else:
        print("Not found")
