from flask import jsonify,request
from app.database import db
from app.models.user import User
from werkzeug.security import generate_password_hash,check_password_hash

def register_user(user):
    username = user.get('username')
    password = user.get('password')

    session = db.Sessionlocal()

    existing_user = session.query(User).filter(User.Username == username).first()
    
    if(existing_user):
        return f" User: {username} Already Exists",409

    # Valid entries 
    hashed_password = generate_password_hash(password)

    user = User(Username = username ,
                Password_hash = hashed_password)
    
    session.add(user)

    session.commit()

    return f"User : {username} registered",201