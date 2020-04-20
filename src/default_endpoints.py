from flask import Blueprint, jsonify

default_endpoints = Blueprint('default_endpoints', __name__)

@default_endpoints.route('/')
def index():
    return jsonify({'greeting':'Hello World!'})
