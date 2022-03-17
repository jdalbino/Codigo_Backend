from ast import Pass
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError, post_dump
from project.dtos.dto_prueba import ValidadorPrueba, validarUsuarioPrueba
from project.ingrediente_dto import ingredienteRequestDTO, ingredienteResponseDTO
from project.models.ingredientes import Ingrediente
from config import conexion
class IngredientesController(Resource):
    def get(self):
        resultado = conexion.session.query(Ingrediente).all()
        print(resultado)
        ingredientesSerializados = ingredienteResponseDTO().dump(resultado)
        return {
            'message':'Yo soy el get de los ingredientes',
            'content':ingredientesSerializados
        }
    
    def post(self):
        print(request.get_json())

        data = request.get_json()

        
        try:
            
            data_serializada = ingredienteRequestDTO().load(data)
            print(data_serializada)

            nuevoIngrediente = Ingrediente()
            nuevoIngrediente.nombre = data_serializada.get('nombre')

            conexion.session.add(nuevoIngrediente)
            conexion.session.commit()

            ingredienteSerializado = ingredienteResponseDTO().dump(nuevoIngrediente)

            return {
                'message':'Ingrediente creado exitosamente',
                'ingrediente':{}
            },201

        except ValidationError as e:
            return {
                'message':'La Informacion es incorrecta',
                'content': e.args
            },400


        except Exception as e:
            print(e.args[0])
            conexion.session.rollback()
            return {
                'message':'Hubo un error al crear el ingrediente',
                'content':e.args[0]
            },500

class PruebaController(Resource):
    def post(self):

        try:
            data = request.get_json()
            validacion = ValidadorPrueba().load(data)
            print(validacion)
            return {
                    'message':'ok',
                    'data': validacion
                }
        except Exception as e:
            print(e.args)
            return {
                'message':'Hubo un error al crear el ingrediente',
                'content':e.args
            }

    def get(self):
        usuario = {
            'nombre':'Eduardo',
            'apellido':'Manrique',
            'nacionalidad':'Peru',
            'password':'mimamamemima'
        }
        resultado = validarUsuarioPrueba()
        Pass