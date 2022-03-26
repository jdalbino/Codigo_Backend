from flask import request
from flask_restful import Resource
from dto.registro_dto import LoginDTO, RegistroDto, UsuarioResponseDTO
from models.usuarios import Usuario
from config import conexion

class RegistroController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data = RegistroDto().load(body)
            nuevoUsuario = Usuario(**data)

            nuevoUsuario.encriptar_pwd()
            conexion.session.add(nuevoUsuario)
            conexion.session.commit()
            respuesta = UsuarioResponseDTO().dump(nuevoUsuario)
            return {
                "message":"Usuario registrado exitosamente",
                "content":respuesta
            },201
        except Exception as e:
            conexion.session.rollback()
            return {
                "message":"Error al registrar al usuario",
                "content":e.args
            },400
class LoginController(Resource):
    def post(self):
        body = request.get_json()

        try:
            data = LoginDTO().load(body)
            return {
                "message":"Bienvenido"
            }
        except Exception as e:
            return {
                "message":"Credenciales incorrectas"
            }