from flask import Flask
from dotenv import load_dotenv
import os

from app.routes.get_tasks import task_bp
from app.routes.create_task import add_bp
from app.routes.delete_task import delete_bp
from app.routes.update_status import update_bp
from app.database import db
from app.database.db import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_app(test_config = None):

    app = Flask(__name__)

    load_dotenv()

    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')

    app.config["DATABASE_URI"] = "mysql+mysqldb://"f"{db_user}:{db_password}@{db_host}/{db_name}"

    if test_config :
        app.config.update(test_config)

    db.engine = create_engine(
        app.config["DATABASE_URI"]
    )
    print(db.engine.url)

    db.Sessionlocal = sessionmaker(
        bind = db.engine
    )

    Base.metadata.create_all(bind=db.engine) 
        
    app.register_blueprint(task_bp)
    app.register_blueprint(add_bp)
    app.register_blueprint(delete_bp)
    app.register_blueprint(update_bp)

    return app