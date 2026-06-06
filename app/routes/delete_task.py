from flask import Blueprint,jsonify,request

from app.database.db import get_connection
from app.services.remove_task import remove_task

delete_bp = Blueprint('delete_task',__name__)

@delete_bp.route("/tasks/<string:task_name>",methods=['DELETE'])
def deleteTask(task_name):
    retval = remove_task(task_name) 

    if (retval['result'] == 'absent'):
        return jsonify(retval),404 #not found
    elif (retval['result'] == 'failure' ):
        return jsonify(retval),500 #other error
    
    return retval,200 #removed
