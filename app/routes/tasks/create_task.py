from flask import Blueprint,jsonify,request
from flask_jwt_extended import jwt_required
from app.services.task.add_task import add_task

add_bp = Blueprint("add_task",__name__)

@add_bp.route("/tasks",methods=['POST'])
@jwt_required()
def addTask():
    data = request.get_json()  # get whatever is written in json 

    task_ = data.get('task')

    if(not request.is_json):
        return jsonify({
            "message":"Invalid Json"
        }),400
    
    response,status_code = add_task(task_)

    return jsonify(response),status_code
