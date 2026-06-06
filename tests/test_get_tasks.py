import sqlite3

def test_get_tasks_empty(client):

    response = client.get("/tasks")
    
    assert response.status_code == 200

    assert response.get_json() == []

def test_get_tasks_by_status(client):

    with client.application.app_context():

        conn = sqlite3.connect(
            client.application.config["DATABASE"]
        )

        cursor = conn.cursor()

        cursor.execute("PRAGMA table_info(tasks)")
        print(cursor.fetchall())
        
        cursor.execute(
            """
            INSERT INTO tasks
            VALUES (?, ?)
            """,
            ("Task 1", "Completed")
        )

        cursor.execute(
            """
            INSERT INTO tasks
            VALUES (?, ?)
            """,
            ("Task 2", "To do")
        )

        conn.commit()
        conn.close()

    response = client.get(
        "/tasks?status=Completed"
    )

    data = response.get_json()

    assert response.status_code == 200

    assert len(data) == 1

    assert data[0][0] == "Task 1"

    assert data[0][1] == "Completed"

def test_invalid_status(client):

    response = client.get(
        "/tasks?status=Random"
    )

    assert response.status_code == 400