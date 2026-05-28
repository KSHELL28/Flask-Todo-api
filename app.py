from flask import Flask,request,jsonify 

app = Flask(__name__)

tasks = [
            {"task" : "DSA" , "status":"To do" },
            {"task" : "DA" ,"status":"Completed" },
            {"task" : "A" ,"status":"Completed"}
]

@app.route("/")

def welcome():
    return "<h1>Welcome to my App</h1>" 

@app.route("/tasks",methods=['GET'])

def get_tasks():

    status_ = request.args.get('status') 

    if(status_ is None):
        return jsonify(tasks)
                
    req_tasks = [] 

    for i in tasks:
        if(i["status"] == status_):
            req_tasks.append(i)

    return jsonify(req_tasks)         

@app.route("/tasks",methods=['POST'])
def add_task():
    data = request.get_json()  # get whatever is written in json 

    task_ = data['task']
    status_ = "To do" 

    new_task = { "task":task_ , "status":status_}
    tasks.append(new_task)

    return jsonify(
        {
            "message":"Task added",
            "Tasks": tasks 
        }
    )

@app.route("/tasks/<string:task_name>",methods=['DELETE']) 
def remove_task(task_name):

    found = False

    for i in tasks: #search for the task 
        if i['task'] == task_name :
            tasks.remove(i) 
            found = True
            break

    if(found):
        return jsonify(
            {
                "removed":task_name ,
                "message" : "task removed",
                "Tasks" : tasks  
            }
        )
    else:
        return jsonify(
        {
            "message" : "task not found"
        }
    )
    
@app.route("/tasks/<string:task_name>",methods=['PATCH'])
def change_status(task_name):
    data_ = request.get_json() 
    if(data_['status'] not in ["To do" ,"Completed"]):
        return jsonify({"message":"enter valid status"}),400
    status_ = data_['status'] 

    for i in tasks:
        if(i['task'] == task_name): 
            i['status'] = status_ 
            return jsonify({
                "message":"Status changed successfully" ,
                "Task":task_name,
                "status":status_
                }
                ),200
    
    return jsonify({"message":"Task not found"}),404

if __name__ == "__main__": 
    app.run(debug=True)

