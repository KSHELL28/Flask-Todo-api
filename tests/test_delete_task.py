def test_delete_task(client):

    client.post(
        "/tasks",
        json={
            "task": "Learn Flask"
        }
    )

    response = client.delete(
        "/tasks/Learn Flask"
    )

    assert response.status_code == 200

    response = client.get("/tasks")

    tasks = response.get_json()

    assert len(tasks) == 0

def test_delete_missing_task(client):

    response = client.delete(
        "/tasks/DoesNotExist"
    )

    assert response.status_code == 404

def test_delete_only_requested_task(client):

    client.post(
        "/tasks",
        json={
            "task": "Task A"
        }
    )

    client.post(
        "/tasks",
        json={
            "task": "Task B"
        }
    )

    client.delete("/tasks/Task A")

    response = client.get("/tasks")

    tasks = response.get_json()

    assert len(tasks) == 1
    assert tasks[0]["task"] == "Task B"

