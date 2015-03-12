from flask import Flask, render_template
from pymongo import MongoClient
from objects.User import User

flaskApp = Flask(
    __name__,
    template_folder='../templates',
    static_folder='../static')

@flaskApp.route('/hola')
def hola():
	return '<h1>Hola, pepino esto funciona</h1>'

@flaskApp.route('/')
def hello_world():
    user = User()

    return render_template(
        'main.html',
        title='Titulo guapo',
        user=user)