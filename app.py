from flask import Flask,request,jsonify 

app = Flask(__name__)

tasks = []

@app.route("/")
def welcome():
    return "<h1>Welcome to my App</h1>" 

@app.route("/get_tasks",methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route("/add_task",methods=['POST'])
def add_task():
    data = request.get_json()  # get whatever is written in json 

    data['status'] = "To do"
    task = data['task']

    tasks.append(task)

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
        if i == task :
            tasks.remove(task) 
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
    return jsonify(
        {
            "message" : "task not found"
        }
    )
    

if __name__ == "__main__": 
    app.run(debug=True)

