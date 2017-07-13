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

# TO - DO: links from '/' to the other routes

@app.route('/rest_request_example')
def rest_request_example():
    return requests.get("http://ip.jsontest.com").text

if __name__ == '__main__':
    app.run(debug=True);
