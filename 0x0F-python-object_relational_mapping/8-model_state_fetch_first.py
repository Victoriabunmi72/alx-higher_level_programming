#!/usr/bin/python3
"""Script that prints the first State object from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    try:

        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(sys.argv[1],
                                       sys.argv[2],
                                       sys.argv[3]))
    Base.metadata.create_all(engine)

    Session.configure(bind=eng)
    session = Session()
    data = session.query(State).first()
    if data:
        print("{}: {}".format(data.id, data.name))
    else:
        print("Nothing")

    except IndexError:
        print("Usage:{} <user> <password> database"
              .format(sys.argv[1]))
        exit(-1)
