from wsgiref.validate import validator
from config import validador
from models.usuarios import Usuario
from marshmallow_sqlalchemy import auto_field
from marshmallow import validate,fields

class RegistroDto(validador.SQLAlchemyAutoSchema):
    correo = auto_field(validator=validate.Email())
    
    class Meta:
        model = Usuario

class UsuarioResponseDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
class LoginDTO(validador.Schema):
    correo = fields.Email(required=True)
    password = fields.String(required=True)