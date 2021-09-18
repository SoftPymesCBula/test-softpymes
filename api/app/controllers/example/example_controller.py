# -*- coding: utf-8 -*-
#########################################################
# All rights by SoftPymes
# Controller Example
#########################################################

from flask import request, jsonify
from flask.wrappers import Request
from app.exception import InternalServerError
from app.models import ExampleModel
from app import db

class ExampleController:

    @staticmethod
    def get_index():
        try:
            response = {
                'ok': True,
                'message': 'Response OK, method get_index'
            }
            return response
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)

    def save():
        try:
            name = request.json['name']
            identification = request.json['identification']
            description = request.json['description']
            status = request.json['status']

            model = ExampleModel(name, identification, description, status)
            db.session.add(model)
            db.session.commit()
            return jsonify({
                'statusResponse': 'Información guardada correctamente'
            })
        except Exception as e:
            return jsonify({
                'status': e,
                'statusResponse': 'Error al editar la información'
            })

    def get_all():
        try:
            all = ExampleModel.query.all()
            return jsonify(all)
        except Exception as e:
            return jsonify({
                'status': e,
                'statusResponse': 'Error al editar la información'
            })

    def delete(id):
        try:
            model = ExampleModel.query.get(id) 
            db.session.delete(model) 
            db.session.commit() 
            return jsonify({
                'statusResponse': 'Información eliminada correctamente'
            })
        except Exception as e:
            return jsonify({
                'status': e,
                'statusResponse': 'Error al editar la información'
            })

    def update(id):
        try:
            model = ExampleModel.query.get(id) #obtener informacion por su id
            name = request.json['name']
            identification = request.json['identification']
            description = request.json['description']
            status = request.json['status']

            model.name = name
            model.identification = identification
            model.description = description
            model.status = status

            db.session.commit() #confirmacion de actualizacion 
            return jsonify({
                'statusResponse': 'Información guardada exitosamente'
            })
        except Exception as e:
            return jsonify({
                'status': e,
                'statusResponse': 'Error al editar la información'
            })
