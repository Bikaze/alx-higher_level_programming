#!/usr/bin/python3
"""This script adds the State object “Louisiana” to the database
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

    obj = State(name='Louisiana')
    session.add(obj)
    session.commit()
    print(obj.id)
