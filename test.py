from flask import Flask
from pymongo import MongoClient
app = Flask(__name__)

@app.route('/')
def hello_world():
    client = MongoClient()
    db = client.vagrantTests
    users = db.users
    return str(users.find_one()['age'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)