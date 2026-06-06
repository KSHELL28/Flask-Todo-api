def test_add_task(client):

    response = client.post(
        "/tasks",
        json={
            "task": "Learn Flask Testing"
        }
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["message"] == "Task added"

    response = client.get("/tasks")

    tasks = response.get_json()

    assert len(tasks) == 1

def test_add_duplicate_task(client):

    client.post(
        "/tasks",
        json={
            "task": "Learn Flask"
        }
    )

    response = client.post(
        "/tasks",
        json={
            "task": "Learn Flask"
        }
    )

    assert response.status_code == 409

def test_add_task_invalid_json(client):

    response = client.post(
        "/tasks",
        data="hello"
    )

    assert response.status_code == 400