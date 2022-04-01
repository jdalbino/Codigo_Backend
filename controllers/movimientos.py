import imp
from flask_restful import Resource,request
from models.movimientos import Movimiento
from dto.movimiento_dto import MovimientoRequestDTO, MovimientoResponseDTO
from flask_jwt import jwt_required,current_identity
from config import conexion

class MovimientoController(Resource):
    @jwt_required()
    def post(self):
        body = request.get_json()
        try:
            print(current_identity)
            data = MovimientoRequestDTO().load(body)
            data["usuario_id"]=current_identity.id
            nuevoMovimiento = Movimiento(**data)
            conexion.session.add(nuevoMovimiento)
            conexion.session.commit()
            resultado = MovimientoResponseDTO
            return{
                "Message":"Movimiento creado exitosamente",
                "content": resultado
            },201
        except Exception as e:
            conexion.session.rollback()
            return {
                "message":"Error al crear el movimiento",
                "content":e.args
            }
    def get(self):
        current_identity
        movimientos: list[Movimiento]=conexion.session.query(Movimiento).filter_by(usuario_id=current_identity.id).all()

        resultado = MovimientoResponseDTO(many=True).dump(movimientos)

        return{
            "message":"los movimientos son",
            "content": resultado
        }