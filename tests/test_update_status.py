from app.database import db
from app.models.task import Task


def test_update_status(client, auth_headers):

    client.post(
        "/tasks",
        json={
            "task": "Learn Flask"
        },
        headers=auth_headers
    )

    response = client.patch(
        "/tasks/Learn Flask",
        json={
            "status": "Completed"
        },
        headers=auth_headers
    )

    assert response.status_code == 200

    with client.application.app_context():

        session = db.Sessionlocal()

        task = session.query(Task).filter(
            Task.task == "Learn Flask"
        ).first()

        assert task.status == "Completed"

        session.close()


def test_update_invalid_status(client, auth_headers):

    client.post(
        "/tasks",
        json={
            "task": "Learn Flask"
        },
        headers=auth_headers
    )

    response = client.patch(
        "/tasks/Learn Flask",
        json={
            "status": "Random"
        },
        headers=auth_headers
    )

    assert response.status_code == 400


def test_update_missing_task(client, auth_headers):

    response = client.patch(
        "/tasks/DoesNotExist",
        json={
            "status": "Completed"
        },
        headers=auth_headers
    )

    assert response.status_code == 404


def test_update_invalid_json(client, auth_headers):

    response = client.patch(
        "/tasks/Learn Flask",
        data="hello",
        content_type="text/plain",
        headers=auth_headers
    )

    assert response.status_code == 415