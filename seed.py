from msilib.schema import ControlEvent
from models.categorias import Categoria
from config import conexion
from sqlalchemy import or_

def categoriasSeed():
    conexion.session.query(Categoria).filter(or_(Categoria.nombre=='%OCIO',Categoria.nombre=="COMIDA")).first()
    pass