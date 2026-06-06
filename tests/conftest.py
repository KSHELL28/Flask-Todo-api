import pytest
import tempfile
import sqlite3

from app import create_app

@pytest.fixture
def client():

    temp_db = tempfile.NamedTemporaryFile(delete=False)
    temp_db.close()

    app = create_app()

    app.config["TESTING"] = True
    app.config["DATABASE"] = temp_db.name

    with app.app_context():

        conn = sqlite3.connect(
            app.config["DATABASE"]
        )

        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE tasks(
            task TEXT UNIQUE,
            status TEXT
        )
        """)

        conn.commit()
        conn.close()

    with app.test_client() as client:
        yield client