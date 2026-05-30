# FLASK TO DO API

## Features 
* Add Tasks ➕
* Get Tasks 🎣
* Remove Tasks ➖
* Update Task Status ✔️

## Tech Stack used

| <img src="https://github.com/user-attachments/assets/8ac0a6ea-f4d2-47c8-96d4-e4d3356f102a" alt="Flask" width="80"/> | <img src="https://github.com/user-attachments/assets/da45ad73-3e91-4e1a-81e4-16affb35fc9c" alt="Postman" width="80"/> | <img src="https://github.com/user-attachments/assets/bb03b795-c022-406a-be52-ee7698b1b707" alt="SQLite" height="80"/> |
| :---: | :---: | :---: |
| **Flask** | **Postman for API testing** | **SQLite Database** |

## Endpoints

* **`GET /tasks`**
  * Get all tasks 
* **`GET /tasks?status=status_`**
  * Get tasks based on status (either `"To do"` or `"Completed"`).
* **`POST /tasks`**
  * Add task (sent through the request body as a JSON object).
* **`PATCH /tasks/:task_name`**
  * Update status of a task to either `"To do"` or `"Completed"`. Status is sent in the body as a JSON object.
* **`DELETE /tasks/:task_name`**
  * Remove tasks from the list.

> 💡 **Note:** Edge cases are handled with robust exception handling and return the appropriate HTTP status codes.

## 🔮 Future Updates

* 🎨 React frontend for task management
* 🔐 JWT-based authentication and authorization
* 🗄️ Migration to SQLAlchemy ORM
* ☁️ Cloud database with Turso
* 🚀 Deployment on Render
* 🧪 Automated API testing

## Getting Started

To install dependencies and run the application locally:

```bash
pip install -r requirements.txt 
python app.py
