import requests
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

# create Flask app
app = Flask(__name__)

# GET request to ip.jsontest.com
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/rest_request_example')
def rest_request_example():
    return requests.get("http://ip.jsontest.com").text

@app.route('/read_db_SQLAlchemy_example')
def read_db_SQLAlchemy_example():
    return "I want my DB!"

@app.route('/read_db_raw_SQL_example')
def read_db_raw_SQL_example():
    return "I want my DB!"

if __name__ == '__main__':
    app.run(debug=True);
