from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return __file__
 
@app.route('/login', methods=["POST"])
def login():
    if request.get_json() == {'user_name':'oguzhan', 'password':'12345'}:
        return  jsonify({
            'status': True,
            'message': 'login successful',
            'data':{
                'token': 'test-token'
            }
        })
    else:
        return jsonify({
            'status': False,
            'message':"login error",
            'data':{}})

@app.route('/register', methods=['POST'])
def register():
    if request.get_json()['user_name']:
        with open('sampleDatabase.txt', 'w') as handle:
            handle.write(request.get_json()['user_name'])
        return jsonify({
            'status': True,
            'message':"register succesful",
            'data':{}})
    return jsonify({
        'status': False,
        'message':"register fail",
        'data':{}})


def start_server():
    app.run(debug=True, port='5001')

if __name__ == "__main__":
    start_server()