from flask import request
from flask_restful import Resource
from project.models.preparaciones import Preparacion
from project.dtos.preparacion_dto import PreparacionRequestDTO
from config import conexion

class PreparacionesController(Resource):
    def post(self):
        try:
            body = request.get_json()
            data = PreparacionRequestDTO().load(body)
            print(data)
            nuevaPreparacion = Preparacion(**data)
            conexion.session.add(nuevaPreparacion)
            conexion.session.commit()
            return {
                'message':'Preparacion creada exitosamente'
            },201
        except Exception as e:
            conexion.session.rollback()
            return {
                'message':'Hubo un error al crear la preparacion',
                'content': e.args
            }