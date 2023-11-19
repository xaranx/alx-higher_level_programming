#!/usr/bin/python3

"""script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """fonction body"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    state_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in state_to_delete:
        session.delete(state)
    session.commit()
    session.close()
