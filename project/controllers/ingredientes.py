from ast import Pass
from distutils.log import info
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError, post_dump
from project.dtos.dto_prueba import ValidadorPrueba, validarUsuarioPrueba
from project.ingrediente_dto import ingredienteRequestDTO, IngredienteResponseDTO
from project.models.ingredientes import Ingrediente
from config import conexion
class IngredientesController(Resource):
    def get(self):
        resultado = conexion.session.query(Ingrediente).all()
        print(resultado)
        ingredientesSerializados = IngredienteResponseDTO(many=True).dump(resultado)
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

            ingredienteSerializado = IngredienteResponseDTO().dump(nuevoIngrediente)

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
        resultado = validarUsuarioPrueba().dump(usuario)
        return {
            'message':'el usuario es',
            'content': usuario,
            'resultado': resultado
        }
class IngredienteController(Resource):
    def get(self,id):

        ingrediente = conexion.session.query(Ingrediente).filter_by(id=id).first()
        print(ingrediente)
        if ingrediente:
            ingrediente = IngredienteResponseDTO().dump(ingrediente)
            return {
            'id':id,
            'result':ingrediente
            }
        else:
            return {
                'message':'El ingrediente a buscar no existe'
            },404
    def put(self,id):
        ingrediente = conexion.session.query(Ingrediente).filter_by(id=id).first()
        try:
            if ingrediente:
                body = request.get_json()
                data_validada = ingredienteRequestDTO().load(body)
                ingrediente.nombre = data_validada.get('nombre')
                conexion.session.commit()
                resultado = IngredienteResponseDTO().dump(ingrediente)
                return {
                    'message':'Ingrediente actualizado exitosamente',
                    'content':{}
                }
            else:
                return {
                    'message':'Ingrediente a actualizar no existe'
                },404
        except Exception as e:
            return {
                'message':'informacion incorrecta',
                'content':e.args
            },400