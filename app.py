from crypt import methods
from flask import Flask
from datetime import datetime
from flask_restful import Api
from project.controllers.ingredientes import ( IngredientesController,
                                               PruebaController,
                                               IngredienteController)
from config import conexion,validador
from project.controllers.recetas import BuscarRecetaController, RecetasController,RecetaController
from project.controllers.preparaciones import PreparacionesController
from project.controllers.ingredientes_recetas import IngredientesRecetasController
from dotenv import load_dotenv
from os import environ

load_dotenv()

print(environ.get("NOMBRE"))

app= Flask(__name__)
api = Api(app=app)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("DATABASEURL")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

conexion.init_app(app)

validador.init_app(app)

conexion.create_all(app=app)

@app.route('/status',methods=['GET'])
def status():
    return {
        'status':True,
        'date':datetime.now().strftime('%Y-%M-%D %h:%m:%s')
    }
@app.route('/')
def inicio():
    return {
        'message':'BIENVENIDO A MI API'
    }

api.add_resource(IngredientesController,'/ingredientes','/ingrediente')
api.add_resource(PruebaController,'/pruebas')
api.add_resource(IngredienteController,'/ingrediente/<int:id>')
api.add_resource(RecetasController,'/recetas','/receta')
api.add_resource(BuscarRecetaController,'/buscar_receta')
api.add_resource(PreparacionesController,'/preparacion')
api.add_resource(RecetaController,'/receta/<int:id>')
api.add_resource(IngredientesRecetasController,"/ingrediente_receta")

if __name__ == '__main__':
    app.run(debug=True)
