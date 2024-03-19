#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from urllib.parse import quote_plus

pwd = quote_plus("@Mcclent8")
url = f"mysql://bikaze:{pwd}@localhost:3306/hbtn_0e_6_usa"

if __name__ == "__main__":
    engine = create_engine(url)
    Base.metadata.create_all(engine)
