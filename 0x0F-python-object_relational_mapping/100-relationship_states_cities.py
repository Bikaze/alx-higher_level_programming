#!/usr/bin/python3
"""This Script creates a state 'California' with the
    city 'San Francisco' from the database"""

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
    state_obj = State(name="California")
    session.add(City(name="San Francisco", state=state_obj))
    session.commit()
