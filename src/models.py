import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
""" class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {} """
class People(Base):
    __tablename__= "people"
    id= Column(Integer, primary_key=True)
    name= Column(String(250),nullable=False)
    gender= Column(String(250),nullable=False)
    height= Column(String,nullable=False)
    homeworld= Column(Integer,nullable=False)
class Planet(Base):
    __tablename__= "planet"
    id= Column(Integer, primary_key=True)
    name= Column(String(250),nullable=False)
    diameter= Column(Integer,nullable=False)
    gravity= Column(Integer,nullable=False)
    population= Column(Integer,nullable=False)
    rotation_period= Column(Integer,nullable=False)
class Vehicles(Base):
    __tablename__= "vehicles"
    id= Column(Integer, primary_key=True)
    name= Column(String(250),nullable=False)
    max_atmosphering_speed= Column(Integer,nullable=False)
    cargo_capacity= Column(Integer,nullable=False)
    cost_in_credits= Column(Integer,nullable=False)
class Favorites(Base):
    __tablename__= "favorites"
    id= Column(Integer, primary_key=True)
    people_id= Column(Integer,ForeignKey('people.id'))
    planet_id= Column(Integer,ForeignKey('planet.id'))
    vehicles_id= Column(Integer,ForeignKey('vehicles.id'))
    planet = relationship(Planet)
    people = relationship(People)
    vehicule = relationship(Vehicles)
    def to_dict(self):
        return {}
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
