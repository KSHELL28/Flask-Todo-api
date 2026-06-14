from flask import request,jsonify,Blueprint
from flask_jwt_extended import jwt_required

from app.services.task.update_status import update_status

update_bp = Blueprint('update_status',__name__)

@update_bp.route("/tasks/<string:task_name>",methods=['PATCH'])
@jwt_required()
def updateStatus(task_name):
    status = request.get_json()
    status = status.get('status')

    response,status_code = update_status(task_name,status)

    return jsonify(response),status_code 