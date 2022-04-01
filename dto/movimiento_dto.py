from dbm import dumb
from flask import request
from marshmallow_sqlalchemy import auto_field
from config import validador
from dto.categoria_dto import CategoriaResponseDTO
from models.movimientos import Movimiento
from marshmallow import fields

class MovimientoRequestDTO(validador.SQLAlchemyAutoSchema):
    usuario_id = auto_field(dump_only=True)
         
    class Meta:
        include_fk = True
        model = Movimiento

class MovimientoResponseDTO(validador.SQLAlchemyAutoSchema):
    categoria = fields.Nested(nested=CategoriaResponseDTO)
    class Meta:
        model = Movimiento
        include_relationships = True