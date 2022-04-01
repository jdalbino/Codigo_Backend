from os import environ
from flask import request
from flask_restful import Resource
from dto.registro_dto import LoginDTO, RegistroDto, UsuarioResponseDTO
from models.usuarios import Usuario
from config import conexion
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dto.usuario_dto import ResetPasswordRequestDTO

class RegistroController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data = RegistroDto().load(body)
            nuevoUsuario = Usuario(**data)

            nuevoUsuario.encriptar_pwd()
            conexion.session.add(nuevoUsuario)
            conexion.session.commit()
            respuesta = UsuarioResponseDTO().dump(nuevoUsuario)
            return {
                "message":"Usuario registrado exitosamente",
                "content":respuesta
            },201
        except Exception as e:
            conexion.session.rollback()
            return {
                "message":"Error al registrar al usuario",
                "content":e.args
            },400
class LoginController(Resource):
    def post(self):
        body = request.get_json()

        try:
            data = LoginDTO().load(body)
            return {
                "message":"Bienvenido"
            }
        except Exception as e:
            return {
                "message":"Credenciales incorrectas"
            }
class ResetPasswordController(Resource):
    def post(self):
        body = request.get_json()
        # ------------- UTILIZANDO LA LIBRERIA DE PYTHON DE MENSAJERIA ----------------
        # creo una variable en la cual almacenare toda la informacion de mi correo (mensaje)
        mensaje = MIMEMultipart()
        email_emisor = environ.get('EMAIL_EMISOR')
        print(email_emisor)
        email_password = environ.get('EMAIL_PASSWORD')
        try:
            data = ResetPasswordRequestDTO().load(body)
            # validar si existe ese usuario en mi bd
            usuarioEncontrado = conexion.session.query(
                Usuario).filter_by(correo=data.get('correo')).first()
            if usuarioEncontrado is not None:
                # texto = "Hola, este es un mensaje de prueba."
                mensaje['Subject'] = 'Reiniciar contraseña Monedero APP'
                # si queremos un generador de correos con diseño : https://beefree.io/
                html = open('./email_templates/joshua_template.html').read().format(
                    usuarioEncontrado.nombre, usuarioEncontrado.correo, environ.get('URL_FRONT'))

                # siempre que queremos agregar un HTML como texto del mensaje tiene que ir despues del texto ya que primero tratara de enviar el ultimo y si no puede enviara el anterior
                # mensaje.attach(MIMEText(texto, 'plain'))
                mensaje.attach(MIMEText(html, 'html'))

                # inicio el envio del correo
                #                   SERVIDOR      | PUERTO
                # outlook > outlook.office365.com | 587
                # hotmail > smtp.live.com         | 587
                # gmail >   smtp.gmail.com        | 587
                # icloud >  smtp.mail.me.com      | 587
                # yahoo >   smtp.mail.yahoo.com   | 587
                # para los correos de GMAIL https://myaccount.google.com/lesssecureapps
                emisorSMTP = SMTP('smtp.gmail.com', 587)
                emisorSMTP.starttls()
                # se hace el login de mi servidor de correo
                emisorSMTP.login(email_emisor, email_password)
                # envio el correo
                emisorSMTP.sendmail(
                    from_addr=email_emisor,
                    to_addrs=usuarioEncontrado.correo,
                    msg=mensaje.as_string()
                )
                # finalizo la sesion de mi correo
                emisorSMTP.quit()
                print('Correo enviado exitosamente')

            return {
                'message': 'Correo enviado exitosamente'
            }
        except Exception as e:
            return {
                'message': 'Error al enviar el correo',
                'content': e.args
            }

        # ---------------- UTILIZANDO SENDGRID -----------------
        # try:
        #     data = ResetPasswordRequestDTO().load(body)
        #     # validar si existe ese usuario en mi bd
        #     usuarioEncontrado = conexion.session.query(
        #         Usuario).filter_by(correo=data.get('correo')).first()
        #     if usuarioEncontrado is not None:
        #         # tengo que utilizar los correos verificados en sendgrid ya que si uso uno que no esta verificado entonces el correo nunca llegara
        #         print(usuarioEncontrado.correo)
        #         from_email = Email('ederiveroman@gmail.com')
        #         to_email = To(usuarioEncontrado.correo)
        #         subject = 'Reinicia tu contraseña del Monedero App'
        #         content = Content(
        #             'text/plain', 'Hola, has solicitado el reinicio de tu contraseña, haz click en el siguiente link para cambiar, sino has sido tu ignora este mensaje: ....')
        #         mail = Mail(from_email, to_email, subject, content)
        #         envia_correo = sendgrid.client.mail.send.post(
        #             request_body=mail.get())
        #         # el estado de la respuesta de sendgrid
        #         print(envia_correo.status_code)
        #         # el cuerpo de la respuesta de sendgrid
        #         print(envia_correo.body)
        #         # las cabeceras de la respuesta de sendgrid
        #         print(envia_correo.headers)

        #     return {
        #         'message': 'Correo enviado exitosamente'
        #     }
        # except Exception as e:
        #     return {
        #         'message': 'Error al resetear la password',
        #         'content': e.args
        #     }