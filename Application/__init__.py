from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '4f1dcaa6d1491c97cc2a3126795f6436'

from Application import routes

