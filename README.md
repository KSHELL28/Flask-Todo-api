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
![Version](https://img.shields.io/badge/Version-3.0-7B8FF7?style=flat-square)

</div>

---

## ✨ Features

| | Feature |
|---|---|
| ✅ | New User Registration |
| ✅ | User and Password Validation |
| ✅ | User Login using JWT Authentication |
| ✅ | Different Users - Different Tasks |
| ✅ | CRUD Operations on Tasks |
| ✅ | Request validation |
| ✅ | SQLAlchemy ORM integration |
| ✅ | MySQL database support |
| ✅ | Automated testing with Pytest |
| ✅ | Docker Containerization |
---

## 🛠 Tech Stack

### Backend
| Tool | Purpose |
|---|---|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) | Core language |
| ![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white) | Web framework |
| ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D97706?style=flat-square&logo=sqlalchemy&logoColor=white) | ORM layer |
| ![JWT](https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white) | Token Authentication |
| ![Werkzeug](https://img.shields.io/badge/Werkzeug-EA580C?style=flat-square&logo=werkzeug&logoColor=white) | Password Hashing |

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

### Deployement
| Tool | Purpose |
|---|---|
| ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) | Containerization |
| ![Docker Compose](https://img.shields.io/badge/Docker_Compose-1D63ED?style=flat-square&logo=docker&logoColor=white) | Multi-container orchestration |

---

## 📁 Project Structure

```text
TODO_APP/
│
├───app/
│   ├───database/
│   │   
│   ├───models/
│   │   
│   ├───routes/
│   │   ├───tasks/
│   │   │
│   │   └───users/
│   │   
│   ├───services/
│   │   ├───auth/
│   │   │   
│   │   └───task/
│   │      
│   │   
│   └───utils
│   
├───tests
│
├── .env.docker.example
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── README.md
├── requirements.txt
└── run.py
```

---

## 🔌 API Endpoints

### Authentication
| Method | Endpoint | Description |
|:---:|---|---|
| `POST` | `/register` | New User Registration |
| `POST` | `/login` | User login |

### Tasks (Protected)
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
<summary><b>POST</b> &nbsp;— User Login</summary>

<br/>

**Request body**
```json
{
    "username" : "Username123",
    "password" : "Password123"
}
```
- *Note : Currently Valid password is anything more than 5 or more Characters .* 

**Response**
```json
{
    "access_token": "ey...",
    "message": "Logged in successfully",
    "status": "success"
}
```
- *Note : Copy the access_token which will be used for CRUD on tasks* 

</details>

<details>
<summary><b>GET</b> &nbsp;— Retrieve all tasks</summary>

<br/>

* *In Authentication : Set Auth Type to Bearer Token and then paste the Token from the login response*

**Response**
```json
{
    "Result": "Success",
    "Tasks | Status": {
        "Task A": "To do",
        "Task B": "Completed",
    }
}
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
    "Message": "Task removed : Task B",
    "Result": "Success",
    "Tasks | Status": {
        "Task A": "To do",
    }
}
```

</details>

---

## 🚀 Running the Project

### TWO Methods :

<details>
<summary><b>1. Local Setup</b> &nbsp;— Without Docker</summary>

<br/>

**1. Clone the repository**
```bash
git clone https://github.com/KSHELL28/Flask-Todo-api
cd TODO_APP
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure environment variables**

* *Create a `.env` file in the project root (refer .env.example):*

```env
DB_USER=root
DB_PASSWORD=your_password
...
```

**4. Start the server**
```bash
python run.py
```

</details>

---

<details>
<summary><b>2. Docker Setup</b> &nbsp;— if Docker installed</summary>

<br/>

**1. Clone the repository**
```bash
git clone https://github.com/KSHELL28/Flask-Todo-api
cd TODO_APP
```

**2. Configure environment variables**

* *Create a `.env.docker` file in the project root (refer .env.docker.example):*

```bash
cp .env.docker.example .env.docker
```

Open .env.docker and configure the required values:
```env
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=mysql
...
```
* *VERY IMPORTANT NOTE : DB_HOST=mysql should not be changed. Docker Compose automatically creates a network where the Flask container communicates with the MySQL container using the service name mysql.*


**3. Build and Start Containers**

```bash
docker compose up --build
```

* Docker Compose will:

    - Build the Flask application image
    - Pull the MySQL image (if not already available)
    - Create a dedicated Docker network
    - Start the MySQL container
    - Start the Flask container
    - Create persistent database storage using Docker volumes
 
* *NOTE : The application uses a dedicated MySQL container managed through Docker Compose. Database access is handled internally by the application.*

**4. Verify Containers**
* In a new terminal:
```bash
docker ps
```

* Expected containers:
```bash
todo-api
todo-mysql
```

</details>

---

## 🧪 Running Tests

```bash
pytest -v
```
* *If using docker need to run above command in different terminal (Ensure you are doing that in same virtual env as of main folder)*

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

**POST** — Create User:

**Request Body**
```json
{
    "username" : "Username123",
    "password" : "Password123"
}
```

**POST** — User Login:

- *Username and Password as set when registering User .*

**Request Body**
```json
{
    "username" : "Username123",
    "password" : "Password123"
}
```

**Response**
```json
{
    "Access_token": "ey...",
    "Message": "Logged in successfully",
    "Result": "Success"
}
```
- *Note : Copy the access_token which will be used for CRUD on tasks* 

**POST** — Create a task:

* *In Authentication : Set Auth Type to Bearer Token and then paste the Token from the login response*

**Request Body**

```json
{ "task": "Practice Badminton" }
```

**PATCH** — update task status:

* *In Authentication : Set Auth Type to Bearer Token and then paste the Token from the login response*

**Request Body**

```json
{ "status": "Completed" }
```

> **💡 Tip:** Use `:task_name` as a path variable in the URL instead of typing the task name each time. Postman lets you fill it in from the variables panel below the URL bar.
> <img width="941" height="269" alt="Screenshot 2026-06-07 142046" src="https://github.com/user-attachments/assets/ff19bbf0-b3d6-4262-a4e2-09396418bc0f" />

</details>

<details>
<summary><b>GET</b> &nbsp;— Requests with query parameters</summary>

<br/>

* *In Authentication : Set Auth Type to Bearer Token and then paste the Token from the login response*

- **All tasks** — send `GET /tasks` with no body
- **Filter by status** — send `GET /tasks?status=To do` or `GET /tasks?status=Completed`

> **💡 Tip:** Add both status values in Postman's **Params** tab and toggle them with checkboxes — no URL editing required each time.
> <img width="947" height="125" alt="Screenshot 2026-06-07 141540" src="https://github.com/user-attachments/assets/163f54bd-9239-4593-9da0-bc97c672438b" />


| KEY | VALUE |
|---|---|
| `status` | `To do` |
| `status` | `Completed` |

</details>

<details>
<summary><b>DELETE</b> &nbsp;— Delete Request</summary>

<br/>

* *In Authentication : Set Auth Type to Bearer Token and then paste the Token from the login response*

- **Delete a task** — send `DELETE /tasks/task_name_to_be_deleted` or `DELETE /tasks/:task_name`

> **💡 Tip:** Adding ":task_name" in the query we can change task_name from Path_variables in Parameters tab just below the query tab that we used in getting tasks .
> <img width="1066" height="308" alt="image" src="https://github.com/user-attachments/assets/697b5daa-0e64-4c04-a110-0d0248b23e99" />

</details>

---

## 📈 Project Evolution
 
<table>
<tr>
<td width="33%" valign="top">
    
### 🔖 [v1.0](../../releases/tag/v1.0)
- Flask REST API
- SQLite (flat-file, no ORM)
- Basic CRUD operations
</td>
<td width="33%" valign="top">
    
### 🔖 [v2.0](../../releases/tag/v2.0)
- SQLAlchemy ORM
- MySQL (production DB)
- Application Factory (`create_app`)
- Blueprint Architecture
- Service Layer
- Automated Pytest suite
- Isolated SQLite test DB
- Environment variable config
</td>
<td width="33%" valign="top">
    
### 🔖 [v3.0](../../releases/tag/v3.0) — Latest
- JWT Authentication
- User registration & login
- Password hashing (Werkzeug)
- Per-user task isolation
- Docker + Docker Compose
- Multi-container networking
</td>
</tr>
</table>

<div align="center">

### 📌 Project Status

Built to progressively learn backend engineering — REST APIs, ORM persistence, layered architecture,
JWT authentication, test isolation, and Docker containerization.

*Intended as a portfolio and learning project — not designed for production deployment.*

</div>
