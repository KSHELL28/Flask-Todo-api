import sqlite3 
from flask import request,jsonify
from flask_jwt_extended import get_jwt_identity

from app.database import db
from app.models.task import Task
from app.models.user import User
from sqlalchemy.exc import IntegrityError

def add_task(task_name): 
    session = db.Sessionlocal()

    try:
        user_id = int(get_jwt_identity())

        user = session.query(User).filter(User.id == user_id).first()
        task = session.query(Task).filter(Task.task == task_name).first()

        if(task is not None):
            return {
                'Result' : 'Failure',
                'Message' : 'Task Already exists'
            },409

        user.tasks.append(Task(task = task_name,status = 'To do'))

        tasks = {}

        for t in user.tasks:
            tasks[t.task] = t.status

        session.commit()   
        
        return {
                "Result" : 'Success',
                "Message" : f"Task added : {task_name}",
                "Tasks | Status": tasks
            },201
    
    except IntegrityError:
        session.rollback()
        return{
            'Result' : 'Conflict',
            "Message" : "Task already exists"
        },409 #conflict 
    
    finally:
        session.close()