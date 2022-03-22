import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    favourites_planets_id = Column(Integer, ForeignKey('favourites_planets.id'))
    favourites_characters_id = Column(Integer, ForeignKey('favourites_characters.id'))
    favourites_starships_id = Column(Integer, ForeignKey('favourites_starships.id'))

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    image = Column(String(300))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(Integer)
    population = Column(Integer)
    climate = Column(Integer)
    terrain = Column(Integer)
    surface_water = Column(Integer)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    gender = Column(String(20))
    image = Column(String(300))
    height = Column(Integer)
    mass = Column(Float)
    hair_color = Column(Integer)
    skin_color = Column(Integer)
    eye_color = Column(Integer)
    birth_year = Column(Integer)

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    image = Column(String(300))
    class_starships = Column(String(50))
    manufacturer = Column(String(50))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    max_atmospheric_speed = Column(Integer)
    hyperdrive_rating = Column(Float)
    mglt = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(50))
    
class Pilots(Base):
    __tablename__ = 'pilots'
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    starships_id = Column(Integer, ForeignKey('starships.id'))

class Favourites_planets(Base):
    __tablename__ = 'favourites_planets'
    id = Column(Integer, primary_key=True)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

class Favourites_characters(Base):
    __tablename__ = 'favourites_characters'
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

class Favourites_starships(Base):
    __tablename__ = 'favourites_starships'
    id = Column(Integer, primary_key=True)
    starships_id = Column(Integer, ForeignKey('starships.id'))
    user_id = Column(Integer, ForeignKey('user.id'))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')