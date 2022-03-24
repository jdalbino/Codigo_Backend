from config import validador
from project.models.ingredientes_recetas import IngredientesRecetas

class IngredientesRecetasRequestDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = IngredientesRecetas
        include_fk = True