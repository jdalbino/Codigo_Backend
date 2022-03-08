# crear una clase Persona en la cual se guarden su nombre, fecha_nacimiento, nacionalidad, dni, ademas tambien una clase Alumno
#  y una clase Docente en la cual el alumno , a diferencia del docente, tenga una serie de cursos matriculados,
#  y el docente por su parte tenga un numero del seguro social y su cuenta de la CTS.
#  En base a lo visto de herencia codificar las clases y ademas ver si hay algun atributo o metodo que deba de ser privado.
from pydoc import Doc, doc
from tkinter import SEL


class Persona:
    def __init__(self,nombre,fecha_nacimiento,nacionalidad,dni):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
        self.dni = dni

class Alumno(Persona):
    def __init__(self,nombre,fecha_nacimiento,nacionalidad,dni,cursos):

        super().__init__(nombre,fecha_nacimiento,nacionalidad,dni)
        self.cursos = cursos
    def info(self):
        return {
            'nombre': self.nombre,
            'Fecha': self.fecha_nacimiento,
            'nacionalidad': self.nacionalidad,
            'dni': self.dni,
            'cursos': self.cursos,
        }

class Docente(Persona):
    def __init__(self,nombre,fecha_nacimiento,nacionalidad,dni,seguro_social,cuenta_cts):

        super().__init__(nombre,fecha_nacimiento,nacionalidad,dni)
        self.seguro_social = seguro_social
        self.cuenta_cts = cuenta_cts

    def info(self):
        return {
            'nombre': self.nombre,
            'Fecha': self.fecha_nacimiento,
            'nacionalidad': self.nacionalidad,
            'dni': self.dni,
            'Seguro Social': self.seguro_social,
            'cuenta CTA': self.cuenta_cts,
        }


alumnoJuan = Alumno("Juan","08-04-1995","peruana",74501400,["algebra","matematica","calculo"])
docenteDiego = Docente("Diego","04-08-1995","española",45074400,12345678,1029383845)

print("Datos del alumno:",alumnoJuan.info())
print("Datos del Docente:",docenteDiego.info())