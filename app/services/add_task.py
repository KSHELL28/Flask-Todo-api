import sqlite3 
from flask import request,jsonify

from app.database import db
from app.models.task import Task
from sqlalchemy.exc import IntegrityError

def add_task():
    session = db.Sessionlocal()

    data = request.get_json()  # get whatever is written in json 
    
    task_ = data['task']

    try:
        session.add(Task(task = task_,status = 'To do'))
        session.commit()   
 
        tasks = session.query(Task).all()
        
        return {
                "result":'success',
                "message":"Task added",
                "Tasks": [
                    task.to_dict() for task in tasks
                ]
            }#,201
    except IntegrityError:
        return{
            'result':'Conflict',
            "message" : "task already exists"
        }#,409 #conflict 
    
    finally:
        session.close()