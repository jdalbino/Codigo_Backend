from os import environ
from re import A
from flask import Flask, app, render_template
from flask_restful import Api
from controllers.usuarios import LoginController, RegistroController
from config import validador,conexion
from dotenv import load_dotenv
from flask_cors import CORS
from flask_jwt import JWT
from seguridad import autenticador,indentificador

load_dotenv()

app = Flask(__name__)
CORS(app=app)
app.config['SECRET_KEY'] = "secreto"
app.config["SQLALCHEMY_DATABASE_URI"]= environ.get("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

jsonwebtoken = JWT(app=app,authentication_handler=autenticador,identity_handler=indentificador)


api = Api(app=app)
validador.init_app(app)
conexion.init_app(app)

conexion.create_all(app=app)

@app.route('/')
def inicio():
    return render_template('inicio.html', nombre="Eduardo", dia="Jueves", integrantes=["Foca", "Lapagol", "Ruidiaz", "Paolin", "Rayo Advincula"], usuario={
        "nombre": "Juan",
        "direccion": "Las piedritas 105",
        "edad": "40"
    }, selecciones=[{"nombre": "Bolivia", "clasificado": False}, {"nombre": "Brasil", "clasificado": True}, {"nombre": "Chile", "clasificado": False}, {"nombre": "Peru", "timado": True}])


api.add_resource(RegistroController,"/registro")
api.add_resource(LoginController,"/login")

if (__name__ == "__main__"):
    app.run(debug=True, port=8080)
