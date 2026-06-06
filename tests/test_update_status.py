def test_update_status(client):

    client.post(
        "/tasks",
        json={
            "task": "Learn Flask"
        }
    )

    response = client.patch(
        "/tasks/Learn Flask",
        json={
            "status": "Completed"
        }
    )

    assert response.status_code == 200

    response = client.get(
        "/tasks?status=Completed"
    )

    tasks = response.get_json()

    assert len(tasks) == 1

def test_update_invalid_status(client):

    client.post(
        "/tasks",
        json={
            "task": "Learn Flask"
        }
    )

    response = client.patch(
        "/tasks/Learn Flask",
        json={
            "status": "Random"
        }
    )

    assert response.status_code == 400

def test_update_missing_task(client):

    response = client.patch(
        "/tasks/DoesNotExist",
        json={
            "status": "Completed"
        }
    )

    assert response.status_code == 404

def test_update_invalid_json(client):

    response = client.patch(
        "/tasks/Learn Flask",
        data="hello"
    )

    assert response.status_code == 400