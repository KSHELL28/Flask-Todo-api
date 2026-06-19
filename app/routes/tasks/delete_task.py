from flask import Blueprint,jsonify
from flask_jwt_extended import jwt_required

from app.services.task.remove_task import remove_task

delete_bp = Blueprint('delete_task',__name__)

@delete_bp.route("/tasks/<string:task_name>",methods=['DELETE'])
@jwt_required()
def deleteTask(task_name):
    
    response,status_code = remove_task(task_name)

    return jsonify(response),status_code
