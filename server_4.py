from flask import Flask
from flask import request
from flask import jsonify
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/login", methods=['POST'])
def login():
    login_data = login_post(request)
    with open('data/login.txt', 'w+') as handle:
        today = datetime.today()
        handle.write('{today}')
    return login_data


def login_post(user_data):
    user_data = user_data.get_json()
    r = requests.post('http://127.0.0.1:5001/login', json={
        'user_name': user_data['user_name'],
        'password': user_data['password']
    }) 
    return r.json()

@app.route('/getdata',methods=['GET'])
def get_data():
    r = requests.get('http://127.0.0.1:5002/read')
    data = r.json()
    if data["status"]:
        
        return jsonify({"txt": data["data"]})
    return data


def start_server():
    app.run(debug=True, port='5004')

if __name__ == "__main__":
    start_server()