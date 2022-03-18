from crypt import methods
from flask import Flask
from datetime import datetime
from flask_restful import Api
from project.controllers.ingredientes import ( IngredientesController,
                                               PruebaController,
                                               IngredienteController)
from config import conexion,validador
from project.controllers.recetas import RecetasController

app= Flask(__name__)
api = Api(app=app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:juandiego1995@127.0.0.1:3306/recetario'

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

if __name__ == '__main__':
    app.run(debug=True)
