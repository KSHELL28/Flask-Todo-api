# FLASK TO DO API

A RESTful To-Do API built using Flask, SQLAlchemy ORM, and MySQL.

The project follows a layered architecture with Blueprints, Services, Models, and Database modules. It supports CRUD operations, task status management, and automated testing using Pytest.

## Features

- Create Tasks
- Retrieve All Tasks
- Filter Tasks by Status
- Update Task Status
- Delete Tasks
- Request Validation
- SQLAlchemy ORM Integration
- MySQL Database Support
- Automated Testing with Pytest
- Environment Variable Configuration

## Tech Stack

### Backend
- Python
- Flask
- SQLAlchemy

### Database
- MySQL

### Testing
- Pytest
- Postman

### Configuration
- python-dotenv

## Project Structure

```text
TODO_APP/
│
├── app/
│   ├── database/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   └── __init__.py
│
├── tests/
│   ├── conftest.py
│   ├── test_add_task.py
│   ├── test_delete_task.py
│   ├── test_get_tasks.py
│   └── test_update_status.py
│
├── run.py
├── requirements.txt
├── .env
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | `/tasks` | Get all tasks |
| GET | `/tasks?status=Completed` | Filter tasks by status |
| POST | `/tasks` | Create a new task |
| PATCH | `/tasks/<task_name>` | Update task status |
| DELETE | `/tasks/<task_name>` | Delete a task |

## Example Requests

### Create Task

**POST** `/tasks`

Request:

```json
{
    "task": "Practice Badminton"
}
```

Response:

```json
{
    "Tasks": [
        {
            "status": "To do",
            "task": "Practice Badminton"
        }
    ],
    "message": "Task added",
    "result": "success"
}
```

### Get All Tasks

**GET** `/tasks`

Response:

```json
[
    {
        "task": "Practice Badminton",
        "status": "To do"
    }
]
```

### Delete Task

**DELETE** `/tasks/Practice Badminton`

Response:

```json
{
    "Tasks": [],
    "message": "task removed",
    "removed": "Practice Badminton",
    "result": "success"
}
```

## Running the Project

### Clone Repository

```bash
git clone <repository-url>
cd TODO_APP
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_NAME=todo_db
```

### Run Application

```bash
pip install -r requirements.txt 
```

```bash
python run.py
```

## Running Tests

```bash
pytest -v
```

## Project Evolution

### Version 1.0
- Flask REST API
- SQLite Database
- CRUD Operations

### Version 2.0
- Migrated to SQLAlchemy ORM
- Migrated from SQLite to MySQL
- Added Application Factory Pattern
- Added Blueprints and Service Layer Architecture
- Added Automated Testing with Pytest
- Added Environment Variable Configuration

## Project Status

This is an educational backend project built to learn Flask, SQLAlchemy, MySQL, REST API development, and automated testing.

It is intended as a portfolio and learning project and is not designed for production deployment.

