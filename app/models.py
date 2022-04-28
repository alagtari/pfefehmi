from sqlalchemy import   Column, Integer, String ,Boolean
from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(40), unique=True, index=True)
    password = Column(String(200))
    name = Column(String(40))
    role = Column(String(20))
    date = Column(String(200))


class Projet(Base):
    __tablename__ = "projet"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(200))
    date = Column(String(200))
    total_vulnerability = Column(String(200))
    high = Column(Boolean)
    medium = Column(Boolean)
    low = Column(Boolean)

class Dynamicscan(Base):
    __tablename__ = "dynamicscan"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(200))
    status = Column(String(200))
    scanner = Column(String(200))
    date = Column(String(200))
    total = Column(String(200))
    high = Column(Boolean)
    medium = Column(Boolean)
    low = Column(Boolean)

class Infrastructure(Base):
    __tablename__ = "infrastructure"

    id = Column(Integer, primary_key=True, index=True)
    target = Column(String(200))
    status = Column(String(200))
    scanner = Column(String(200))
    date = Column(String(200))
    total = Column(String(200))
    high = Column(Boolean)
    medium = Column(Boolean)
    low = Column(Boolean)


class Connectors(Base):
    __tablename__ = "connectors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    status = Column(String(200))
    date = Column(String(200))


