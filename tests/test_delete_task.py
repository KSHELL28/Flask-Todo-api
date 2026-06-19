from app.database import db
from app.models.task import Task


def test_delete_task(client, auth_headers):

    client.post(
        "/tasks",
        json={"task": "Learn Flask"},
        headers=auth_headers
    )

    response = client.delete(
        "/tasks/Learn Flask",
        headers=auth_headers
    )

    assert response.status_code == 200


def test_delete_missing_task(client, auth_headers):

    response = client.delete(
        "/tasks/DoesNotExist",
        headers=auth_headers
    )

    assert response.status_code == 404


def test_delete_only_requested_task(client, auth_headers):

    client.post(
        "/tasks",
        json={"task": "Task A"},
        headers=auth_headers
    )

    client.post(
        "/tasks",
        json={"task": "Task B"},
        headers=auth_headers
    )

    client.delete(
        "/tasks/Task A",
        headers=auth_headers
    )

    response = client.get(
        "/tasks",
        headers=auth_headers
    )

    data = response.get_json()

    assert "Task A" not in data["Tasks | Status"]
    assert "Task B" in data["Tasks | Status"]