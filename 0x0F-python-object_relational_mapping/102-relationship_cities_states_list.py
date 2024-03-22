#!/usr/bin/python3
"""This is a script that lists all City objects from the database
    hbtn_0e_101_usa"""

import sys
from relationship_city import City, Base
from relationship_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from urllib.parse import quote_plus

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], quote_plus(sys.argv[2]),
                                   sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City):
        print(f"{city.id}: {city.name} -> {city.state.name}")
