#!/usr/bin/python3
"""This is a script that changes the name of a State object from the
    database
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

    obj = session.get(State, 2)
    if obj:
        obj.name = "New Mexico"
        session.commit()
