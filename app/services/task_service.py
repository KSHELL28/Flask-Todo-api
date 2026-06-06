from flask import request
from app.database.db import get_connection
from app.utils.validators import is_valid_status

def get_all_tasks():
    
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    conn.close()
    return tasks

def get_task_by_status():
    conn = get_connection()
    cursor = conn.cursor() 

    status_ = request.args.get('status')

    if(not is_valid_status(status_)):
        conn.close()
        return ({
            "message":"Invalid status"
        }) #,400
    
    cursor.execute("select * from tasks where status = ?",
                   (status_,))
    tasks = cursor.fetchall()

    conn.close()
    return tasks #,200