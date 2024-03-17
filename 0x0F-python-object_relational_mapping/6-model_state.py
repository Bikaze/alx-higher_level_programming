#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
# from urllib.parse import quote_plus
# 
# pwd = quote_plus("@Mcclent8")
# url = f"mysql://bikaze:{pwd}@localhost:3306/hbtn_0e_6_usa"
# engine = create_engine(url)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
