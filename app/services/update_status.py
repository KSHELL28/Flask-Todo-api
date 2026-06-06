from flask import request
import sqlite3
from app.utils.validators import is_valid_status
from app.database import db
from app.models.task import Task

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
    
    session = db.Sessionlocal()

    status_ = data_['status'] 

    try:
        task = session.query(Task).where(Task.task == task_name).first()
        
        if task is None:
            session.close()
            return {
                'result':'Absent',
                "message" :" Task not found"
            }#,404
        
        # IF FOUND THEN Updated AND COMMIT
        session.query(Task).where(Task.task == task_name).update({Task.status : status_})

        session.commit()
        
        tasks = session.query(Task).all()

        return {
            'result':'Success',
            "message" : "Task updated successfully",
            "Tasks" : [
                task.to_dict() for task in tasks
            ]
        }#,200

    except Exception as e:
        return {
            'result':'Failure',
            "message" : "unexpected error occured"
        }
    
    finally:
        session.close()
