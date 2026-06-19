import pytest
import tempfile

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token

from app import create_app
from app.database import db
from app.database.db import Base
from app.models.user import User


@pytest.fixture
def client():

    temp_db = tempfile.NamedTemporaryFile(delete=False)
    temp_db.close()

    app = create_app({
        "DATABASE_URI": f"sqlite:///{temp_db.name}",
        "TESTING": True
    })

    with app.app_context():

        Base.metadata.create_all(bind=db.engine)

        yield app.test_client()

        Base.metadata.drop_all(bind=db.engine)


@pytest.fixture
def auth_headers(client):

    with client.application.app_context():

        session = db.Sessionlocal()

        user = User(
            Username="testuser",
            Password_hash=generate_password_hash("password123")
        )

        session.add(user)
        session.commit()

        token = create_access_token(
            identity=str(user.id)
        )

        session.close()

        return {
            "Authorization": f"Bearer {token}"
        }