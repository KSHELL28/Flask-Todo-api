from flask import Blueprint, jsonify,request

from app.services.task_service import get_all_tasks,get_task_by_status
from app.utils.validators import is_valid_status

task_bp = Blueprint("tasks",__name__)

@task_bp.route("/tasks",methods=['GET'])
def get_tasks():
    
    status = request.args.get("status")

    if(status is None):
        tasks=get_all_tasks()
        return jsonify(tasks),200 #ALL
    
    if(not is_valid_status(status)):
        return jsonify({
            'message':'Invalid status' #INVALID
        }),400 
    
    tasks = get_task_by_status() 
    return jsonify(tasks),200 #on status

    






