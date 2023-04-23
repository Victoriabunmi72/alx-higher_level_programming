#!/usr/bin/python3
"""State object from the database hbtn+0e_6_usa"""
import sys
from sqlachemy import (create_engine)
from sqlachemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "
--main__":
      eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(sys.argv[1], sys.argv[2],
                                sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(eng)
    session = sessionmaker(bind=eng)
    session = session()
    for i in session.query(State).order_by(State.id).all():
        print(f"{i.id}: {i.name}")
    session.close
