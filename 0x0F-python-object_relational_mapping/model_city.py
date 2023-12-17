#!/usr/bin/python3
'''Module for the City
'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from model_state import Base


class City(Base):
    '''Representation of a row in cities table
    '''
    __tablename__ = "cities"
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
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )
    state = relationship('State', back_populates='cities')
