from flask import Blueprint

default_endpoints = Blueprint('default_endpoints', __name__)

@default_endpoints.route('/')
def index():
    return "Hello World!"
