from flask import Flask
from pymongo import MongoClient
flaskApp = Flask(__name__)

@flaskApp.route('/hola')
def hola():
	return '<h1>Hola, pepino esto funciona</h1>'

@flaskApp.route('/')
def hello_world():
    client = MongoClient()
    db = client.vagrantTests
    users = db.users
    return str(users.find_one()['age'])

if __name__ == '__main__':
    flaskApp.run(host='0.0.0.0', debug=True)