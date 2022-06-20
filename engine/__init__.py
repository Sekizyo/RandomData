from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'FH8a9sh9128h34h'

from engine import routes

app.run()