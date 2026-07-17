from sqlalchemy import String,Integer,ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped,mapped_column,relationship
from dotenv import load_dotenv
import os

from app.database.db import Base

load_dotenv()
varchar_size = int(
    os.getenv("VAR_SIZE", "50")
)

class Task(Base):
    __tablename__= "tasks"

    # Composite primary key: same task name is allowed for different users
    task : Mapped[str] = mapped_column(
        String(varchar_size),
        primary_key=True
    )

    user_id : Mapped[int] = mapped_column(
        Integer,
        ForeignKey('users.id'),
        primary_key=True   # <-- second part of composite PK
    )

    status : Mapped[str] = mapped_column(
        String(varchar_size),
        nullable=False
    )

    user : Mapped["User"] = relationship(back_populates='tasks')

    # Composite PK (task, user_id) means:
    #   - Same user cannot have two tasks with the same name
    #   - Different users CAN have tasks with the same name ✓

    def to_dict(self):
        return {
            "task": self.task,
            "status": self.status
        }
