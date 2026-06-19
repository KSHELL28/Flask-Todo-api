from flask import request
from flask_jwt_extended import get_jwt_identity

from app.database import db
from app.models.task import Task
from app.models.user import User
from app.utils.validators import is_valid_status

def get_all_tasks():

    session = db.Sessionlocal() 

    try :

        user_id = int(get_jwt_identity()) # Gets the userid for this user

        user = session.query(User).where(User.id == user_id).first()

        tasks = {}

        for t in user.tasks:
            tasks[t.task] = t.status

        return {
            'Result':'Success',
            "Tasks | Status" : tasks
        },200

    finally:    
        session.close()
   
def get_task_by_status(status):

    session = db.Sessionlocal()

    try:
        user_id = int(get_jwt_identity()) # Gets the userid for this user

        if(not is_valid_status(status)):
            return {
                'Result' : 'Failure',
                "Message" : "Invalid status"
            },400
        
        user = session.query(User).where(User.id == user_id).first() #can use .filter also

        tasks = {}

        for t in user.tasks :
            if(t.status == status):
                tasks[t.task] = t.status

        return {
            "Result" : "Success",
            "Message" : "Tasks fetched successfully",
            "Tasks | Status" : tasks
        },200
    
    finally:
        session.close() 