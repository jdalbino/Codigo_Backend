from pyexpat import model
from random import choice
from config import validador
from project.models.preparaciones import Preparacion
from project.models.recetas import Receta
from marshmallow import fields,validate

class RecetaRequestDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model= Receta
        
class RecetaResponseDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Receta

class BuscarRecetaRequestDto(validador.Schema):
    nombre = fields.String(required=False)
    estado = fields.Boolean(required=False)
    comensales = fields.Integer(required=False)
    dificultad = fields.String(required=False,validate=validate.OneOf(choices=['FACIL','INTERMEDIO','DIFICIL','EXTREMO']))


class PreparacionResponseDTO(validador.SQLAlchemyAutoSchema):
     class Meta:
         model = Preparacion

class RecetaPreparacionesResponseDTO(validador.SQLAlchemyAutoSchema):
     preparaciones = fields.Nested(nested=PreparacionResponseDTO,many=True,only=['description','orden'])
     class Meta:
         model = Receta