from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

valid_Statuses = ["To do" , "Completed"]

@app.route("/")

def welcome():
    return "<h1>Welcome to my App</h1>" 

@app.route("/tasks",methods=['GET'])

def get_tasks():

    conn = sqlite3.connect("Todo.db") 
    cursor = conn.cursor()

    status_ = request.args.get('status') 

    if(status_ is None):
        cursor.execute("select * from tasks ;" )
        tasks = cursor.fetchall() 

        conn.close()    
        return jsonify(tasks),200

    if(status_ not in valid_Statuses):
        conn.close()
        return jsonify({
            "message":"Invalid status"
        }),400
    
    cursor.execute("select * from tasks where status = ?",
                   (status_,))
    tasks = cursor.fetchall()

    conn.close()
    return jsonify(tasks),200         

@app.route("/tasks",methods=['POST'])
def add_task():
    conn = sqlite3.connect("Todo.db")
    cursor = conn.cursor()

    data = request.get_json()  # get whatever is written in json 
    if(not request.is_json):
        return jsonify({
            "message":"Invalid Json"
        }),400
    
    task_ = data['task']

    try:
        cursor.execute(
            "insert into tasks(task,status) values (?,?)",
            (task_ ,"To do")
        )
        conn.commit()    

        cursor = cursor.execute("select * from tasks") 
        tasks = cursor.fetchall()
        return jsonify(
            {
                "message":"Task added",
                "Tasks": tasks 
            }
        ),201
    except sqlite3.IntegrityError:
        return jsonify(
            {"message" : "task already exists"
        }),409 #conflict 
    
    finally:
        conn.close()



@app.route("/tasks/<string:task_name>",methods=['DELETE']) 
def remove_task(task_name):
    conn = sqlite3.connect("Todo.db")
    cursor = conn.cursor()
    try :
        cursor.execute(
            """delete from tasks 
            where task = ? """,
            (task_name,)
            )
        if(cursor.rowcount == 0):
            return jsonify({
                "message":"Task not found"
            }),404
        conn.commit()
        cursor = cursor.execute("select * from tasks")
        tasks = cursor.fetchall()
        return jsonify(
            {
                "removed":task_name ,
                "message" : "task removed",
                "Tasks" : tasks  
            }),200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    finally:
        conn.close()
    
@app.route("/tasks/<string:task_name>",methods=['PATCH'])
def change_status(task_name):

    if not request.is_json:
        return jsonify({
        "message": "Request must be JSON"
    }), 400

    data_ = request.get_json() 

    if(data_['status'] not in valid_Statuses):
        return jsonify({"message":"enter valid status"}),400
    
    conn = sqlite3.connect("Todo.db")
    cursor = conn.cursor()

    status_ = data_['status'] 

    try:
        cursor = cursor.execute("""update tasks
                       set status = ?
                       where task = ?
                       """,
                       (status_,task_name))
        
        if cursor.rowcount == 0:
            conn.close()
            return jsonify({
                "message" :" Task not found"
            }),404
        
        # IF FOUND THEN DELETED AND COMMIT
        conn.commit()
        
        cursor = cursor.execute("select * from tasks")
        tasks = cursor.fetchall()

        conn.close()
        return jsonify({
            "message" : "Task updated successfully",
            "Tasks" : tasks
        }),200

    except Exception as e:
        conn.close()
        return jsonify ({
            "message" : "unexpected error occured"
        }),500


if __name__ == "__main__": 
    app.run(debug=True)

