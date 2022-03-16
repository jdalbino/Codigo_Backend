from crypt import methods
from flask import Flask
from datetime import datetime
from flask_restful import Api
from project.controllers.ingredientes import IngredientesController
from config import conexion

app= Flask(__name__)
api = Api(app=app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/recetario'

conexion.init_app(app)

conexion.create_all(app=app)

@app.route('/status',methods=['GET'])
def status():
    return {
        'status':True,
        'date':datetime.now().strftime('%Y-%M-%D %h:%m:%s')
    }

api.add_resource(IngredientesController,'/ingredientes','/ingrediente')

if __name__ == '__main__':
    app.run(debug=True)
