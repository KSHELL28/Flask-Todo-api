from flask import Flask
from flask_jwt_extended import JWTManager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

from app.models.user import User
from app.models.task import Task
from app.routes.tasks.get_tasks import task_bp
from app.routes.tasks.create_task import add_bp
from app.routes.tasks.delete_task import delete_bp
from app.routes.tasks.update_status import update_bp
from app.routes.users.register_user import register_bp
from app.routes.users.login import login_bp
from app.database import db
from app.database.db import Base

def create_app(test_config = None):

    app = Flask(__name__)

    load_dotenv()

    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')
    SECRET_Key = os.getenv('secret_key')

    app.config['DATABASE_URI'] = "mysql+mysqldb://"f"{db_user}:{db_password}@{db_host}/{db_name}"
    app.config['JWT_SECRET_KEY'] = f"{SECRET_Key}"

    jwt = JWTManager(app)

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
    app.register_blueprint(register_bp)
    app.register_blueprint(login_bp)

    return app