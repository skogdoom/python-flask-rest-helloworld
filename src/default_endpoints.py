from flask import Blueprint, jsonify, request

default_endpoints = Blueprint('default_endpoints', __name__)

@default_endpoints.route('/')
def index():
    name_param = request.args.get('name')

    if name_param is None:
        return jsonify({'greeting':'Hello World!'})
    else:
        return jsonify({'greeting':'Hello {0}'.format(name_param)})
