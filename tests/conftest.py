import pytest
import tempfile
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import db
from app.database.db import Base

from app import create_app

@pytest.fixture
def client():

    temp_db = tempfile.NamedTemporaryFile(delete=False)
    temp_db.close()

    test_engine = create_engine(
        f"sqlite:///{temp_db.name}"
    )

    app = create_app({
        "DATABASE_URI":
        f"sqlite:///{temp_db.name}"
    })

    with app.app_context():

        Base.metadata.create_all(bind = test_engine)

    with app.test_client() as client:
        yield client