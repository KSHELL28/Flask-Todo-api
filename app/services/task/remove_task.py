from flask import request
from flask_jwt_extended import get_jwt_identity
import sqlite3
from app.database import db
from app.models.task import Task
from app.models.user import User

def remove_task(task_name):
    
    session = db.Sessionlocal()

    try :
        user_id = get_jwt_identity()

        user = session.query(User).filter(User.id == user_id).first() # get user
        task = session.query(Task).filter(Task.task == task_name).first() # get task

        if(task is None):
            return{
                'Result' : 'Failure',
                'Message' : 'Task not Found'
            },404

        session.delete(task)

        session.commit()
        
        tasks = {}
        for t in user.tasks:
            tasks[t.task] = t.status

        return{
                'Result':'Success',
                "Message" : f"Task removed : {task_name}",
                "Tasks | Status" : tasks
            },200
    
    
    except Exception as e:
        session.rollback()
        return {
            'Result':'Failure',
            "Error": str(e)
            },500
    
    finally:
        session.close()