from flask import Flask
from flask import request
from datetime import datetime

app = Flask(__name__)

@app.route("/save_txt")
def save_txt():
    with open("data/{datetime.today}.txt", 'w+') as handle:
        handle.write(request.data['txt'])

def start_server():
    app.run(debug=True, port='5003')

if __name__ == "__main__":
    start_server()