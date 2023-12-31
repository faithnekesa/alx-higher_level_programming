#!/usr/bin/python3
'''Script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


if __name__ == '__main__':
    if len(sys.argv) >= 5:
        user = sys.argv[1]
        pword = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]
        chk = map(lambda x: x.isalpha() or (x in (' ', '%', '_')), state_name)
        if not all(chk):
            state_name = ''
        DATABASE_URL = "mysql://{}:{}@localhost:3306/{}".format(
            user, pword, db_name
        )
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()
        result = session.query(State).filter(State.name == state_name).first()
        if result is not None:
            print('{}'.format(result.id))
        else:
            print('Not found')
