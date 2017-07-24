import requests
import MySQLdb
import os
from flask import Flask
from flask import render_template

# create Flask app
app = Flask(__name__)

# GET request to ip.jsontest.com
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/rest_request_example')
def rest_request_example():
    return requests.get("http://ip.jsontest.com").text

@app.route('/read_db_SQL_example')
def read_db_SQL_example():
    cursor = get_db().cursor()
    sql = "SELECT * FROM SampleTable"
    cursor.execute(sql)
    results = cursor.fetchall()
    rows = ""
    for row in results:
        rows = rows + ','.join(row) + "<br/>"
    return rows

def get_db():
    my_user = os.environ["MYSQLCS_USER_NAME"]
    my_passwd = os.environ["MYSQLCS_USER_PASSWORD"]
    my_host, port_db = os.environ["MYSQLCS_CONNECT_STRING"].split(":")
    my_port_str, my_db = port_db.split("/")
    my_port = int(my_port_str)
    return MySQLdb.connect(host=my_host,
        user=my_user,
        passwd=my_passwd,
        port=my_port,
        db=my_db)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=int(os.environ["PORT"]))
