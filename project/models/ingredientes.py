from sqlalchemy import Column,types
from config import conexion
class Ingrediente(conexion.Model):
    id = Column(type_=types.Integer,primary_key=True,autoincrement=True)
    nombre = Column(type_=types.String(45),nullable=False,unique=True)

    __tablename__ = 'ingredientes'