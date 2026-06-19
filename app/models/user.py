from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import String

from app.database.db import Base

class User(Base):
    __tablename__ = "users"

    id : Mapped[int] = mapped_column(primary_key=True,autoincrement=True)

    Username : Mapped[str] = mapped_column(String(15),unique=True,nullable=False)

    Password_hash : Mapped[str] = mapped_column(String(255),nullable=False) 

    tasks : Mapped[list["Task"]] = relationship(back_populates='user')

    # The purpose of back_populates is to establish bi-directional synchronization in Python's memory. It tells SQLAlchemy: "When I modify this relationship attribute on one object, automatically update the corresponding relationship attribute on the other object."       





