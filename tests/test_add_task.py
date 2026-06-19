from app.database import db
from app.models.task import Task


def test_add_task(client, auth_headers):

    response = client.post(
        "/tasks",
        json={
            "task": "Learn Flask Testing"
        },
        headers=auth_headers
    )

    assert response.status_code == 201

    with client.application.app_context():

        session = db.Sessionlocal()

        task = session.query(Task).filter(
            Task.task == "Learn Flask Testing"
        ).first()

        assert task is not None
        assert task.status == "To do"

        session.close()


def test_add_duplicate_task(client, auth_headers):

    client.post(
        "/tasks",
        json={
            "task": "Learn Flask"
        },
        headers=auth_headers
    )

    response = client.post(
        "/tasks",
        json={
            "task": "Learn Flask"
        },
        headers=auth_headers
    )

    assert response.status_code == 409


def test_add_task_invalid_json(client, auth_headers):

    response = client.post(
        "/tasks",
        data="hello",
        content_type="text/plain",
        headers=auth_headers
    )

    assert response.status_code == 415