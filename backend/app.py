from flask import Flask, request
import flask
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
idDict = {"idCounter" : 5}

def getCurrentID(idCounter):
    idCounter = idCounter + 1
    return idCounter


@app.route("/")
def hello():
    return "Hello, World!"

""" @app.route('/users', methods=["GET"])
def users():
    print("users endpoint reached...")
    with open("users.json", "r") as f:  # reading a file
        data = json.load(f)  # deserialization

    data["id4"] = {"username":"user4", "password":"pass4"}  # modifying the python object

    with open("users.json", "w") as f:
        json.dump(data, f)  # serializing back to the original file
    return data  """

@app.route('/users', methods=["GET", "POST"])
def users():
    print("users endpoint reached...")
    if request.method == "GET":
        with open("users.json", "r") as f:  # reading a file
            data = json.load(f)  # deserialization

        data["id4"] = {"username":"user4", "password":"pass4"}  # modifying the python object

        with open("users.json", "w") as f:
            json.dump(data, f)  # serializing back to the original file
        return data
    if request.method == "POST":
        #currentID = "id" + str(getCurrentID(idDict["idCounter"])) #currentID and idCounter somehow work if it uses a dictionary
        #print(f"currID: {currentID}")
        received_data = request.get_json()
        currentID = list(received_data.keys())[0]
        print(f"received data: {received_data}")
        message = received_data[currentID]
        return_data = {
            "status": "success",
            "message": f"received: {message}"
        }

        # saving sent data to json
        with open("users.json", "r") as f:  # reading a file
            data = json.load(f)  # deserialization
        print(f"data: {data}")
        print(f"recdata: {received_data}")
        data[currentID] = received_data[currentID] #message  # modifying the python object
        #idCounter += 1 # increment
        with open("users.json", "w") as f:
            json.dump(data, f)  # serializing back to the original file

        return flask.Response(response=json.dumps(return_data), status=201)

if __name__ == "__main__":
    app.run("localhost", 6969)