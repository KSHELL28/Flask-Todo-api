from app.database.db import engine
from app.models.task import Task
from app.database.db import Base

Base.metadata.create_all(engine)

