from flask import Flask
from controllers.wakeup import wake_pc

app = Flask(__name__)    

@app.route("/")
def hello():
    return print_help()

@app.route("/wake-desktop")
def wake_desktop():
    wake_pc("04:d9:f5:1b:30:72")
    return {
        "Message": "Success"
    }

def print_help():
    return {
        "Available Routes": [
            "/wake-desktop"
        ]
    }

def start_server():
    app.run(host="0.0.0.0")