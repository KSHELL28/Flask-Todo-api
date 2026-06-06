from app.database import db
from app.models.task import Task

def test_get_tasks_empty(client):

    response = client.get("/tasks")
    
    assert response.status_code == 200

    assert response.get_json() == []

def test_get_tasks_by_status(client):

    with client.application.app_context():

        session = db.Sessionlocal()
        
        session.add(Task(task = 'Task 1',status = 'Completed'))
        session.commit() 

        session.add(Task(task = 'Task 2',status = 'To do'))
        session.commit() 

        session.close()

    response = client.get(
        "/tasks?status=Completed"
    )

    data = response.get_json()

    assert response.status_code == 200

    assert len(data) == 1

    assert data[0]["task"] == "Task 1"
    assert data[0]["status"] == "Completed"

def test_invalid_status(client):

    response = client.get(
        "/tasks?status=Random"
    )

    assert response.status_code == 400