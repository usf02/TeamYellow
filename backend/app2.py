from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

# Define the directory where uploaded files will be stored
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_files():
    # Check if the POST request has the file part
    if 'pdfFiles' not in request.files and 'jpgFiles' not in request.files:
        return jsonify({'message': 'No file part'})

    pdf_files = request.files.getlist('pdfFiles')
    jpg_files = request.files.getlist('jpgFiles')
    uploaded_files = []

    for file in pdf_files + jpg_files:
        if file.filename != '':
            # Generate a unique filename to prevent overwriting
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            i = 1
            while os.path.exists(filename):
                filename = os.path.join(app.config['UPLOAD_FOLDER'], f"{i}_{file.filename}")
                i += 1
            file.save(filename)
            uploaded_files.append(file.filename)

    return jsonify({'message': 'Files uploaded successfully', 'uploaded_files': uploaded_files})

# Define the path to the JSON file where user data will be stored
USER_DATA_FILE = 'user_data.json'

# Create an empty list to hold user data
users = []

# Load existing user data from the JSON file
try:
    with open(USER_DATA_FILE, 'r') as file:
        users = json.load(file)
except FileNotFoundError:
    # If the file doesn't exist, create an empty list
    users = []

def save_user_data():
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users, file)

@app.route('/createUser', methods=['GET','POST'])
def create_user():
    data = request.form  # Retrieve form data

    username = data.get("username")
    password = data.get("password")

    # Check if username already exists
    if any(user == username for user in users):
        response = {
            'message': 'Username already exists. Please choose another username.'
        }
    else:
        # Store user data in the list
        users.append({"username": username, "password": password})
        save_user_data()  # Save user data to the JSON file

        response = {
            'message': f'User "{username}" created successfully.'
        }

    return flask.jsonify(response)



if __name__ == '__main__':
    app.run("localhost", 5000)
