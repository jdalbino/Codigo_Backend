from sqlalchemy import Column,types
from config import conexion

class Categoria(conexion.Model):
    __tablename__="categorias"

    id = Column(type_=types.Integer,primary_key=True,autoincrement=True)
    nombre = Column(type_=types.String(length=45),nullable=False)