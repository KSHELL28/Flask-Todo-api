from flask import request,jsonify,Blueprint

from app.services.update_status import update_status

update_bp = Blueprint('update_status',__name__)

@update_bp.route("/tasks/<string:task_name>",methods=['PATCH'])
def updateStatus(task_name):
    retval = update_status(task_name)

    if(retval['result'] == 'Invalid JSON'):
        return jsonify(retval),400
    
    if(retval['result'] == 'Invalid status'):
        return jsonify(retval),400
    
    if(retval['result'] == 'Absent'):
        return jsonify(retval),404
    
    if(retval['result'] == 'Failure'):
        return jsonify(retval),500
    
    return jsonify(retval),200