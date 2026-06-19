from flask import jsonify,request
from app.database import db
from app.models.user import User
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy.exc import IntegrityError

def register_user(user):
    username = user.get('username')
    password = user.get('password')

    session = db.Sessionlocal()
    try:
        # Username validation
        if(username == ""):
            return {
                'result':'Failure',
                'message':'Username cannot be empty'
            },400
        
        # Password Validation
        
        if(password == ""):
            return {
                'result':'Failure',
                'message':'Password cannot be empty'
            },400
        
        if(len(password) <= 4):
            return {
                'result':'Failure',
                'message':'Password must be more than 4 characters'
            },400

        hashed_password = generate_password_hash(password)

        user = User(Username = username ,
                    Password_hash = hashed_password)
        
        session.add(user)
        session.commit()

        return f"User : {username} registered",201
    
    except IntegrityError:
        return{
            'result':'Conflict',
            "message" : "username already exists"
        },409 #conflict 
    
    finally:
        session.close() 