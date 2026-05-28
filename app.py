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

@app.route("/get_all_tasks",methods=['GET'])
def get_all_tasks():
    return jsonify(tasks)

@app.route("/get_tasks",methods=['GET'])
def get_tasks():
    status_ = request.args.get('status') 
        
    req_tasks = [] 

    for i in tasks:
        if(i["status"] == status_):
            req_tasks.append(i)

    return jsonify(req_tasks)         

@app.route("/add_task",methods=['POST'])
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

@app.route("/remove_task",methods=['DELETE']) 
def remove_task():

    task_to_delete = request.get_json() #delete karaycha task

    found = False

    task = task_to_delete['task']

    if(task == ""):
        return jsonify(
            {
                "message":"enter valid task"
            }
        )

    for i in tasks: #search for the task 
        if i['task'] == task :
            tasks.remove(i) 
            found = True
            break

    if(found):
        return jsonify(
            {
                "removed":task ,
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
    
@app.route("/change_status/<string:task_name>",methods=['PATCH'])
def Change_status(task_name):
    data_ = request.get_json() 
    status_ = data_['status'] 
    if(status_ not in ["To do" ,"Completed"]):
        return jsonify({"message":"enter valid status"})

    for i in tasks:
        if(i['task'] == task_name): 
            i['status'] = status_ 
            return jsonify({
                "Tasks":tasks,
                "message":"Status changed successfully"})
    
    return jsonify({"message":"Task not found"})

if __name__ == "__main__": 
    app.run(debug=True)

