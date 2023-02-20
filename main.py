from flask import Flask
import sys
from waitress import serve
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__=='__main__':
    serve(app,port=os.environ.get('SERVER_PORT',"8088"))

