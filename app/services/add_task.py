import sqlite3 
from flask import request,jsonify

from app.database.db import get_connection

def add_task():
    conn = get_connection()
    cursor = conn.cursor()

    data = request.get_json()  # get whatever is written in json 
    
    task_ = data['task']

    try:
        cursor.execute(
            "insert into tasks(task,status) values (?,?)",
            (task_ ,"To do")
        )
        conn.commit()    

        cursor = cursor.execute("select * from tasks") 
        tasks = cursor.fetchall()
        return {
                "result":'success',
                "message":"Task added",
                "Tasks": tasks 
            }#,201
    except sqlite3.IntegrityError:
        return{
            'result':'failure',
            "message" : "task already exists"
        }#,409 #conflict 
    
    finally:
        conn.close()