""""
Basic test code for Flask
"""
from flask import Flask

app= Flask(__name__)

@app.route('/')
def index():
    return ("Hello World")

@app.route('/warmup')
def warmup():
    return ("warmup")

@app.route('/test')
def test():
    return ("test")

if __name__=="__main__":
    app.run(debug=True)