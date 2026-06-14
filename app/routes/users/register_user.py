from flask import Blueprint,jsonify,request
from app.services.auth.register_user import register_user

register_bp = Blueprint("register",__name__)

@register_bp.route("/register",methods=['POST'])
def register():
    user = request.get_json()

    response, status_code = register_user(user)

    return jsonify(response),status_code 
    