import sqlite3
from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase

class Base(DeclarativeBase):
    pass

engine = None

Sessionlocal = None
