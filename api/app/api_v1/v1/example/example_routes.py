# -*- coding: utf-8 -*-
#########################################################
# All rights by SoftPymes
# Routes Example
#########################################################

from flask import request, jsonify
from flask.wrappers import Response
from app.api_v1 import api
from app.controllers import ExampleController as Controller


@api.route('/index', methods=['GET'])
def get_index():
    response = Controller.get_index()
    return jsonify(data=response)

@api.route('/example', method=['POST'])
def save():
    res = Controller.save()
    return jsonify(res)

@api.route('/example<id>', method=['DELETE'])
def delete(id):
    res = Controller.delete(id)
    return jsonify(res)

@api.route('/example<id>', method=['PUT'])
def update(id):
    res = Controller.update(id)
    return jsonify(res)


