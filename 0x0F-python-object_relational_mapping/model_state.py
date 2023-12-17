#!/usr/bin/python3
'''A module for he State model
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()
'''Representation of the base class for all tables
'''


class State(Base):
    '''Representation for a row in a states table
    '''
    __tablename__ = "states"
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(
        String(length=128),
        nullable=False
    )
