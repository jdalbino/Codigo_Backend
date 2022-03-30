from ast import Pass
from config import conexion
from models.usuarios import Usuario
from bcrypt import checkpw

def autenticador(username,password):
    
    if username and password:
        usuarioEncontrado = conexion.session.query(Usuario).filter_by(correo=username).first()
        if usuarioEncontrado:
            validacion = checkpw(bytes(password,"utf-8"),bytes(usuarioEncontrado.password,"utf-8"))
            if validacion is True:
                print("si es la contraseña")
                return usuarioEncontrado
            else:
                return None
        else:
            return None
    else:
        return None
    
def indentificador(payload):
    print(payload)
    usuarioEncontrado: Usuario | None = conexion.session.query(Usuario).filter_by(id=payload["identity"]).first()
    if usuarioEncontrado:
        return {
            "id":usuarioEncontrado.id,
            "nombre":usuarioEncontrado.nombre,
            "correo":usuarioEncontrado.correo
            }
    else:
        return None