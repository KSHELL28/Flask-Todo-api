from sqlalchemy import String
from sqlalchemy.orm import Mapped,mapped_column
from dotenv import load_dotenv
import os

from app.database.db import Base

load_dotenv()
varchar_size = int(os.getenv('VAR_SIZE'))

class Task(Base):
    __tablename__= "tasks"

    task : Mapped[str] = mapped_column(
        String(varchar_size),
        primary_key=True
    )  

    status : Mapped[str] = mapped_column(
        String(varchar_size),
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


