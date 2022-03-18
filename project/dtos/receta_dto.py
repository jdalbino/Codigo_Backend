from pyexpat import model
from config import validador
from project.models.recetas import Receta

class RecetaRequestDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model= Receta
        
class RecetaResponseDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Receta