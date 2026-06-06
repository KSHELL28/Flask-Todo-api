from flask import request,jsonify
import sqlite3
from app.database.db import get_connection

def remove_task(task_name):
    conn = get_connection()
    cursor = conn.cursor()
    try :
        cursor.execute(
            """delete from tasks 
            where task = ? """,
            (task_name,)
            )
        if(cursor.rowcount == 0):
            return {
                'result':'absent',
                "message":"Task not found"
            }#,404
        
        conn.commit()

        cursor = cursor.execute("select * from tasks")
        tasks = cursor.fetchall()

        return{
                'result':'success',
                "removed":task_name ,
                "message" : "task removed",
                "Tasks" : tasks  
            }#,200
    
    except Exception as e:
        return ({
            'result':'failure',
            "error": str(e)
            })#, 500
    
    finally:
        conn.close()