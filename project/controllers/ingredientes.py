from flask import request
from flask_restful import Resource
from models.ingredientes import Ingrediente
class IngredientesController(Resource):
    def get(self):
        return {
            'message':'Yo soy el get de los ingredientes'
        }
    def post(self):
        print(request.get_json())
        return {
            'message':'Yo soy el post'
        }