from sqlalchemy import String
from sqlalchemy.orm import Mapped,mapped_column

from app.database.db import Base

class Task(Base):
    __tablename__= "tasks"

    task : Mapped[str] = mapped_column(
        String,
        primary_key=True
    )  

    status : Mapped[str] = mapped_column(
        String,
        nullable=False
    )

# ^^^^^^^^^^^^^^^^^Replaces CREATE TABLE tasks(
#                  Task TEXT PRIMARY KEY,
#                  Status TEXT NOT NULL
#                  )

    def to_dict(self):
        return {
            "task": self.task,
            "status": self.status
        }


