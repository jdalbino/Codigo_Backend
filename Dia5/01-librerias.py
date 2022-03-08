from cgitb import text
import imp
from camelcase import CamelCase 

instanciaCC = CamelCase("mundo","backend")

texto = "Bienvenido al mundo del backend mi amigo"

print(instanciaCC.hump(texto))