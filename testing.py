from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello Team 2!</p>"

@app.route("/settings")
def settings():
    return "<p>settings</p>"    
