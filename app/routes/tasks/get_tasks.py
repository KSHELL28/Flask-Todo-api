from flask import Blueprint, jsonify,request
from flask_jwt_extended import jwt_required,get_jwt_identity

from app.services.task.task_service import get_all_tasks,get_task_by_status
from app.utils.validators import is_valid_status

task_bp = Blueprint("tasks",__name__)

@task_bp.route("/tasks",methods=['GET'])
@jwt_required()
def get_tasks():
    
    status = request.args.get("status")

    if(status is None):
        response,status_code=get_all_tasks()
        return jsonify(response),status_code #ALL
    
    response,status_code = get_task_by_status(status) 

    return jsonify(response),status_code 

    






