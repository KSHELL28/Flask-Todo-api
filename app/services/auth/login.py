from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import NoResultFound

from app.database import db 
from app.models.user import User

def login_user(data):    
    username = data.get('username')
    password = data.get('password')

    session = db.Sessionlocal()

    try:
        user = session.query(User).filter(User.Username == username).first()    

        if(user is None): #if user is not found
            return {
                'Result' : 'Failure',
                'Message' : 'User not found'
            },401
        
        # user is valid check password
        # password is valid and user is also valid login now 
        if not check_password_hash(user.Password_hash,password) :
            return {
                'Result' : 'Failure',
                'Message' : 'Wrong Password , Try again .'
            },401 
        
        token = create_access_token(identity=str(user.id))

        return {
            'Result' : 'Success',
            "Access_token" : token,
            'Message' : 'Logged in successfully'
        },200
    
    finally:
        session.close()


