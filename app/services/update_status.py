from flask import request,jsonify
import sqlite3
from app.utils.validators import is_valid_status
from app.database.db import get_connection

def update_status(task_name):

    if not request.is_json:
        return {
            'result':'Invalid JSON',
            "message": "Request must be JSON"
    }#, 400

    data_ = request.get_json() 

    if(not is_valid_status(data_['status'])):
        return {
            'result':'Invalid status',
            "message":"enter valid status"
            }#,400
    
    conn = get_connection()
    cursor = conn.cursor()

    status_ = data_['status'] 

    try:
        cursor = cursor.execute("""update tasks
                       set status = ?
                       where task = ?
                       """,
                       (status_,task_name))
        
        if cursor.rowcount == 0:
            conn.close()
            return {
                'result':'Absent',
                "message" :" Task not found"
            }#,404
        
        # IF FOUND THEN DELETED AND COMMIT
        conn.commit()
        
        cursor = cursor.execute("select * from tasks")
        tasks = cursor.fetchall()

        conn.close()
        return {
            'result':'Success',
            "message" : "Task updated successfully",
            "Tasks" : tasks
        }#,200

    except Exception as e:
        conn.close()
        return {
            'result':'Failure',
            "message" : "unexpected error occured"
        }#,500
