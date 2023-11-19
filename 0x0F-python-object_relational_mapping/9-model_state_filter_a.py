#!/usr/bin/python3

"""lists all State objects that contain
the letter a from the database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """function body"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)\
                                 .filter(State.name.like('%a%'))
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
