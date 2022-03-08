from crypt import methods
from distutils.log import debug
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

clientes = []

@app.route("/")
def estado():
    hora_del_servidor = datetime.now()
    return {
        "status": True,
        "hour": hora_del_servidor.strftime("%d/%m/%Y %H:%M:%S")
    }

@app.route("/clientes", methods=['GET','POST'])
def getcliente():
    print(request.method)
    print(request.get_json())
    data = request.get_json()
    clientes.append(data)
    return {
        "status": "Cliente agregado exitosamente",
        "client": data
    }

app.run(debug=True)