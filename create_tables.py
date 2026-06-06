from app import create_app

from app.models.task import Task
from app.database import db

app = create_app()

with app.app_context():
    db.Base.metadata.create_all(bind=db.engine)

print("Tables created")

