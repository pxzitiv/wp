from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_Alexander():
    return 'Hello, World!'
