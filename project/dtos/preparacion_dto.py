from pyexpat import model
from xml.etree.ElementInclude import include
from config import validador
from project.dtos.receta_dto import RecetaResponseDTO
from project.models.preparaciones import Preparacion
from marshmallow_sqlalchemy import auto_field
from marshmallow import fields

from project.models.recetas import Receta

class PreparacionRequestDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Preparacion
        include_fk = True

class RecetaResponseDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model=Receta

class PreparacionResponseDTO(validador.SQLAlchemyAutoSchema):
    receta = fields.Nested(nested=RecetaResponseDTO,data_key='receta_relacion')
    class Meta:
        model = Preparacion
        load_instance = True
        include_fk = False
        include_relationships = True