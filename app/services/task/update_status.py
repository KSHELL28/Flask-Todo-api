from flask import request
from flask_jwt_extended import get_jwt_identity
import sqlite3

from app.utils.validators import is_valid_status
from app.database import db
from app.models.task import Task
from app.models.user import User

def update_status(task_name,status):

    if not request.is_json:
        return {
            'Result' : 'Invalid JSON',
            "Message" : "Request must be JSON"
    },400

    if not is_valid_status(status):
        return {
            'Result' : 'Invalid status',
            "Message" : "Enter valid status"
            },400
    
    session = db.Sessionlocal()
    try:
        user_id = get_jwt_identity()

        user = session.query(User).filter(User.id == user_id).first() # get user
        task = session.query(Task).where(Task.task == task_name).first()
        
        if task is None:
            session.close()
            return {
                'Result' : 'Absent',
                "Message" :"Task not found"
            },404
        
        # IF FOUND THEN Updated AND COMMIT
        session.query(Task).where(Task.task == task_name).update({Task.status : status})

        session.commit()
        
        tasks = {}
        for t in user.tasks:
            tasks[t.task] = t.status

        return {
            'Result' : 'Success',
            "Message" : f"Task : {task_name} updated to {status} successfully",
            "Tasks | Status" : tasks
        },200

    except Exception as e:
        return {
            'Result' : 'Failure',
            "Message" : "Unexpected error occured"
        },500
    
    finally:
        session.close()
