from flask import Blueprint,jsonify,request

from app.services.add_task import add_task

add_bp = Blueprint("add_task",__name__)

@add_bp.route("/tasks",methods=['POST'])
def addTask():
    
    if(not request.is_json):
        return jsonify({
            "message":"Invalid Json"
        }),400
    
    task_ = add_task()

    if(task_['result'] == 'success'):
        return jsonify(task_),201
    
    return jsonify(task_),409 
