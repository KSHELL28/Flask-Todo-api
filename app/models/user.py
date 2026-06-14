from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String
from app.database.db import Base

class User(Base):
    __tablename__ = "users"

    id : Mapped[int] = mapped_column(primary_key=True,autoincrement=True)

    Username : Mapped[str] = mapped_column(String(15),unique=True,nullable=False)

    Password_hash : Mapped[str] = mapped_column(String(255),nullable=False) 

    # ^^^^^^^^^^^^^^^^^Replaces CREATE TABLE users(
    #                  username TEXT PRIMARY KEY,
    #                  password TEXT NOT NULL
    #                  )





