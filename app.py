from flask import Flask, jsonify, request 
app = Flask(__name__)

tasks = [
    {
        'id':1,
        'name': 'vanshika',
        'contact': 'happy@gmail.com',
        'Done': False
    }
]

@app.route("/")
def hey_there():
    return "hey there"

@app.route("/add-data", methods = ["POST"])
def addTask():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data"
        },400)
    task = {
            'id': tasks[-1]['id'] + 1,
            'name': request.json['name'],
            'contact': request.json.get('description', ""),
            'Done': False

    }
    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "Task added successfully"
    })
@app.route("/get-data")
def getTask():
    return jsonify({
        "data": tasks
    })
if (__name__=="__main__"):
    app.run(debug = True)