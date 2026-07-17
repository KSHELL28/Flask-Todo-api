from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker
import pymysql
import os
from dotenv import load_dotenv
import time

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

    import urllib.parse

    db_user = os.getenv("DB_USER", "root")
    db_password_raw = os.getenv("DB_PASSWORD", "password")
    db_password = urllib.parse.quote_plus(db_password_raw)
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "3306")
    db_name = os.getenv("DB_NAME", "todo_db")

    SECRET_Key = os.getenv(
        "secret_key",
        "development-secret-key-change-me"
    )

    app.config['DATABASE_URI'] = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    app.config['JWT_SECRET_KEY'] = f"{SECRET_Key}"

    jwt = JWTManager(app)

    # Allow requests from React dev server and production Vercel deployment
    allowed_origins = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        os.getenv("FRONTEND_URL", ""),
    ]
    CORS(app, resources={r"/*": {"origins": [o for o in allowed_origins if o]}},
         supports_credentials=False)

    if test_config :
        app.config.update(test_config)

    db.engine = create_engine(
        app.config["DATABASE_URI"]
    )
    print(db.engine.url)

    db.Sessionlocal = sessionmaker(
        bind = db.engine
    )


    for attempt in range(20):
        try:
            with db.engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            break

        except Exception:
            print(f"Waiting for database... ({attempt + 1}/20)")
            time.sleep(2)

    Base.metadata.create_all(bind=db.engine) 
        
    app.register_blueprint(task_bp)
    app.register_blueprint(add_bp)
    app.register_blueprint(delete_bp)
    app.register_blueprint(update_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(login_bp)

    return app