from multiprocessing import context
from flask_restful import Resource,request
from project.models.recetas import Receta
from project.dtos.receta_dto import RecetaRequestDTO, RecetaResponseDTO
from config import conexion

class RecetasController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data = RecetaRequestDTO().load(body)
            nuevaReceta = Receta(
                nombre = data.get('nombre'),
                estado = data.get('estado'),
                comensales = data.get('comensales'),
                duracion = data.get('duracion'),
                dificultad = data.get('dificultad')
            )
            conexion.session.add(nuevaReceta)
            conexion.session.commit()
            return {
                'message':'Receta creada exitosamente'
            },201

        except Exception as e:
            conexion.session.rollback()
            return {
                'message':'Error al crear la receta',
                'content':e.args
            },404
    def get(self):
        recetas = conexion.session.query(Receta).all()
        respuesta = RecetaResponseDTO(many=True).dump(recetas)
        return {
            'message':'Las recetas son:',
            'content':respuesta
        }