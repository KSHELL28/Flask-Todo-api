<div align="center">

# 📝 Flask To-Do API

**A RESTful To-Do API built with Flask, SQLAlchemy ORM, and MySQL.**

Layered architecture with Blueprints, Services, Models, and Database modules.
Supports full CRUD operations, task status management, and automated testing.

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D97706?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-00758F?style=for-the-badge&logo=mysql&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

<br/>

![Status](https://img.shields.io/badge/Status-Educational%20Project-5CE4B4?style=flat-square)
![Version](https://img.shields.io/badge/Version-2.0-7B8FF7?style=flat-square)

</div>

---

## ✨ Features

| | Feature |
|---|---|
| ✅ | Create tasks |
| ✅ | Retrieve all tasks |
| ✅ | Filter tasks by status |
| ✅ | Update task status |
| ✅ | Delete tasks |
| ✅ | Request validation |
| ✅ | SQLAlchemy ORM integration |
| ✅ | MySQL database support |
| ✅ | Automated testing with Pytest |
| ✅ | Environment variable configuration |

---

## 🛠 Tech Stack

### Backend
| Tool | Purpose |
|---|---|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) | Core language |
| ![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white) | Web framework |
| ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D97706?style=flat-square&logo=sqlalchemy&logoColor=white) | ORM layer |

### Database
| Tool | Purpose |
|---|---|
| ![MySQL](https://img.shields.io/badge/MySQL-00758F?style=flat-square&logo=mysql&logoColor=white) | Primary database |

### Testing
| Tool | Purpose |
|---|---|
| ![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white) | Automated test suite |
| ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white) | Manual API testing |

### Configuration
| Tool | Purpose |
|---|---|
| ![dotenv](https://img.shields.io/badge/python--dotenv-ECD53F?style=flat-square&logo=dotenv&logoColor=black) | Environment variables |

---

## 📁 Project Structure

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

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|:---:|---|---|
| `GET` | `/tasks` | Get all tasks |
| `GET` | `/tasks?status=Completed` | Filter tasks by status |
| `POST` | `/tasks` | Create a new task |
| `PATCH` | `/tasks/<task_name>` | Update task status |
| `DELETE` | `/tasks/<task_name>` | Delete a task |

---

## 💡 Example Requests

<details>
<summary><b>POST</b> &nbsp;— Create a task</summary>

<br/>

**Request body**
```json
{
    "task": "Practice Badminton"
}
```

**Response**
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

</details>

<details>
<summary><b>GET</b> &nbsp;— Retrieve all tasks</summary>

<br/>

**Response**
```json
[
    {
        "task": "Practice Badminton",
        "status": "To do"
    }
]
```

</details>

<details>
<summary><b>DELETE</b> &nbsp;— Remove a task</summary>

<br/>

**Request**
```
DELETE /tasks/Practice Badminton
```

**Response**
```json
{
    "Tasks": [],
    "message": "task removed",
    "removed": "Practice Badminton",
    "result": "success"
}
```

</details>

---

## 🚀 Running the Project

**1. Clone the repository**
```bash
git clone <repository-url>
cd TODO_APP
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure environment variables**

Create a `.env` file in the project root:
```env
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_NAME=todo_db
```

**4. Start the server**
```bash
python run.py
```

---

## 🧪 Running Tests

```bash
pytest -v
```

---

## 📮 Manual Testing with Postman

After starting the server, the API is available at `http://127.0.0.1:5000`.

<details>
<summary><b>POST &amp; PATCH</b> &nbsp;— Requests with a body</summary>

<br/>

1. Open Postman and create a new request
2. Select `POST` or `PATCH` as the method
3. Enter the endpoint URL
4. Go to **Body → raw → JSON** and enter the payload

**POST** — create a task:
```json
{ "task": "Practice Badminton" }
```

**PATCH** — update task status:
```json
{ "status": "Completed" }
```

> **💡 Tip:** Use `:task_name` as a path variable in the URL instead of typing the task name each time. Postman lets you fill it in from the variables panel below the URL bar.
> <img width="941" height="269" alt="Screenshot 2026-06-07 142046" src="https://github.com/user-attachments/assets/ff19bbf0-b3d6-4262-a4e2-09396418bc0f" />

</details>

<details>
<summary><b>GET</b> &nbsp;— Requests with query parameters</summary>

<br/>

- **All tasks** — send `GET /tasks` with no body
- **Filter by status** — send `GET /tasks?status=To do` or `GET /tasks?status=Completed`

> **💡 Tip:** Add both status values in Postman's **Params** tab and toggle them with checkboxes — no URL editing required each time.
> <img width="947" height="125" alt="Screenshot 2026-06-07 141540" src="https://github.com/user-attachments/assets/163f54bd-9239-4593-9da0-bc97c672438b" />


| KEY | VALUE |
|---|---|
| `status` | `To do` |
| `status` | `Completed` |

</details>

---

## 📈 Project Evolution

<table>
<tr>
<td width="50%">

### 🔖 Version 1.0
- Flask REST API
- SQLite database
- Core CRUD operations

</td>
<td width="50%">

### 🔖 Version 2.0 — Current
- Migrated to SQLAlchemy ORM
- Migrated from SQLite to MySQL
- Application Factory Pattern
- Blueprints & Service Layer
- Automated Pytest suite
- Environment variable configuration

</td>
</tr>
</table>

---

<div align="center">

### 📌 Project Status

This is an **educational backend project** built to learn Flask, SQLAlchemy, MySQL,
REST API development, and automated testing.

*Intended as a portfolio and learning project — not designed for production deployment.*

</div>
