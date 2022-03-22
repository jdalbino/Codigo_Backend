from config import conexion
from sqlalchemy import Column,types,orm
from sqlalchemy.sql.schema import ForeignKey

class Preparacion(conexion.Model):
    id = Column(type_=types.Integer,autoincrement=True,primary_key=True)
    description = Column(type_=types.String(length=45))
    orden = Column(type_=types.Integer,nullable=False)

    receta_id=Column(ForeignKey(column='recetas.id'),type_=types.Integer)
    recetas = orm.relationship('Receta',backref='preparaciones')

    __tablename__ = 'preparaciones'