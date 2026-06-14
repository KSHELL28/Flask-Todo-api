from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

from app.database import db 
from app.models.user import User

def login_user(data):    
    username = data.get('username')
    password = data.get('password')

    session = db.Sessionlocal()

    user = session.query(User).filter(User.Username == username).first()

    if(user is None):
        return "Invalid Credentials !",401
    
    # user is valid check password
    if not check_password_hash(user.Password_hash,password) :
        return "Wrong Password , Try Again",401 
    
    # password is valid and user is also valid login now 
    token = create_access_token(identity=str(user.id))

    return f"access_token : {token}",200


