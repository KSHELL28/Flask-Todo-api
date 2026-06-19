from app.database import db
from app.models.task import Task
from app.models.user import User


def test_get_tasks_empty(client, auth_headers):

    response = client.get(
        "/tasks",
        headers=auth_headers
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["Tasks | Status"] == {}


def test_get_tasks_by_status(client, auth_headers):

    with client.application.app_context():

        session = db.Sessionlocal()

        user = session.query(User).first()

        session.add(
            Task(
                task="Task 1",
                status="Completed",
                user_id=user.id
            )
        )

        session.add(
            Task(
                task="Task 2",
                status="To do",
                user_id=user.id
            )
        )

        session.commit()
        session.close()

    response = client.get(
        "/tasks?status=Completed",
        headers=auth_headers
    )

    assert response.status_code == 200

    data = response.get_json()

    assert "Task 1" in data["Tasks | Status"]
    assert "Task 2" not in data["Tasks | Status"]


def test_invalid_status(client, auth_headers):

    response = client.get(
        "/tasks?status=Random",
        headers=auth_headers
    )

    assert response.status_code == 400