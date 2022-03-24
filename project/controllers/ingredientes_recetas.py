from flask import request
from flask_restful import Resource
from itsdangerous import exc
from project.models.ingredientes_recetas import IngredientesRecetas
from config import conexion
from project.dtos.ingredientes_Recetas_dto import IngredientesRecetasRequestDTO

class IngredientesRecetasController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data= IngredientesRecetasRequestDTO().load(body)
            nuevoIR = IngredientesRecetas(**data)
            conexion.session.add(nuevoIR)
            conexion.session.commit()
            return {
                "message":"Realizado",
                "content": nuevoIR
            }
        
        except Exception as e:
            conexion.session.rollback()
            return {
                "message":"Error al ingresar el ingredientes-recetas",
                "content": e.args
            }
        pass