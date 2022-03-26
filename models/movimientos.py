from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer,types,orm
from config import conexion

class Movimiento(conexion.Model):
    __tablename__ = "movimientos"

    id = Column(type_=Integer, primary_key=True,autoincrement=True)
    monto = Column(type_=types.Float(),nullable=False)
    tipo = Column(type_=types.Enum("INGRESO","EGRESO"),nullable=False)
    descripcion = Column(type_=types.String(45))
    moneda = Column(type_=types.Enum("SOLES","DOLARES","EUROS"))
    fecha_creaciones = Column(type_=types.DateTime(),default=datetime.now())

    usuario_id = Column(ForeignKey(column="usuarios_id"),type_=types.Integer,nullable=False)
    
    usuario = orm.relationship("Usuario",backref="usuario_movimientos")

    categoria_id = Column(ForeignKey(column="categorias.id"),type_=types.Integer,nullable=False)

    categoria = orm.relationship("Categoria",backref="categoria_movimientos")