from flask import request,jsonify,Blueprint
from app.services.auth.login import login_user

login_bp = Blueprint("login",__name__)

@login_bp.route("/login",methods=['POST'])
def login():
    data = request.get_json()

    response,status_code = login_user(data)

    return jsonify(response),status_code