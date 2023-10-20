from flask import Flask
import flask
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/users', methods=["GET"])
def users():
    print("users endpoint reached...")
    with open("users.json", "r") as f:  # reading a file
        data = json.load(f)  # deserialization

    data["id4"] = {"username":"user4", "password":"pass4"}  # modifying the python object

    with open("users.json", "w") as f:
        json.dump(data, f)  # serializing back to the original file
    return data 

if __name__ == "__main__":
    app.run("localhost", 6969)