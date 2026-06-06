from flask import request

from app.database import db
from app.models.task import Task
from app.utils.validators import is_valid_status

def get_all_tasks():

    session = db.Sessionlocal()

    try:
        tasks = session.query(Task).all()

        return [
            task.to_dict() for task in tasks  
        ]
    
    finally:
        session.close()
   
def get_task_by_status():

    session = db.Sessionlocal()

    status_ = request.args.get('status')

    try:
        tasks = session.query(Task).where(Task.status == status_).all() #can use .filter also

        return [
            task.to_dict() for task in tasks 
        ] #,200
    except:
        if(not is_valid_status(status_)):
            return ({
                "message":"Invalid status"
            }) #,400
    finally:
        session.close() 