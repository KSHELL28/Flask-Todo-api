from flask import request
import sqlite3
from app.database import db
from app.models.task import Task

def remove_task(task_name):
    
    session = db.Sessionlocal()

    try :
        task = session.query(Task).filter(
            Task.task == task_name
        ).first()

        if task is None:
            return {
                'result':'absent',
                "message":"Task not found"
            },404

        session.delete(task)

        session.commit()
        
        tasks = session.query(Task).all()

        return{
                'result':'success',
                "removed":task_name ,
                "message" : "task removed",
                "Tasks" : [
                    task.to_dict() for task in tasks
                ]  
            },200
    
    
    except Exception as e:
        session.rollback()
        return {
            'result':'failure',
            "error": str(e)
            },500
    
    finally:
        session.close()