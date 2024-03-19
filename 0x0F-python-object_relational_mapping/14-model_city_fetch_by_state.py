#!/usr/bin/python3
"""This is a script that prints all City objects from the database
   hbtn_0e_14_usa
"""
import sys
from model_state import State, Base
from model_city import City
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
    cty = session.query(City.id, City.name, State.name) \
        .join(State, City.state_id == State.id)
    for city in cty.all():
        print(f"{city[2]}: ({city[0]}) {city[1]}")
