from flask import current_app
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

engine = None

Sessionlocal = None
