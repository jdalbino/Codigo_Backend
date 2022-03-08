# para evitar el salto de linea en una impresion de pantalla print() podemos declarar un parametro end=''
# print('hola',end='*')
# print('estos son los ejercicios')
# Escriba una funcion que le pida al usuario ingresar la altura y el ancho de un rectangulo y que lo dibuje usando *, ejemplo:
# altura: 5
# ancho: 4
# Resultado:
# ****
# ****
# ****
# ****
# ****
# dibujar_rectangulo()

def dibujar_rectangulo():
    alto = int(input("Alto:"))
    ancho = int(input("Ancho:"))
    row = ""
    
    for ancho_num in range(ancho):
        row+= "*"
    for num_alto in range(alto):
          print(row)

dibujar_rectangulo()

# Escribir una funcion que nosotros le ingresemos el grosor de un octagono y que lo dibuje
# Ejemplo:
# Grosor: 5             row = ""
#       *****           for i in range(5) row = "*****"
#      *******              ' '*(i-1) + "i*"*"" + *(i-1)
#     *********             
#    ***********          
#   *************
#   *************
#   *************
#   *************
#   *************
#    ***********
#     *********
#      *******
#       *****
# dibujar_octagono()
def dibujar_octagono():
    oct = int(input("Grosor:"))
    # PARTE SUPERIOR
    for i in range(oct):
        print(' ' * (oct - i - 1) + '*' * (oct + i * 2))
    # PARTE MEDIO
    for i in range(oct-1):
        print('*' * (oct + (oct - 1) * 2))
    # PARTE BAJA
    for i in range(oct-1):
        if i == 0:
            print(' ' + '*' * ((oct - i + 2) * 2))
        else:
             print(' ' * (i+1) + '*' * ((oct - i + 2) * 2))

dibujar_octagono()
# Ingresar un numero entero y ese numero debe de llegar a 1 usando la serie de Collatz
# si el numero es par, se divide entre dos
# si el numero es impar, se multiplica por 3 y se suma 1
# la serie termina cuando el numero es 1
# Ejemplo 19
# 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
# serie_collatz()
def serie_collatz():
    numero = int(input("Numero:"))
    resultado = []
    calculando = ""
    if (numero % 2 == 0):
        while True:
                if numero == 1 or numero == 0:
                    calculando = numero
                    resultado.append(calculando)
                    print(calculando)
                    numero = calculando
                    break
                else:
                    calculando = numero/2
                    resultado.append(calculando)
                    print(calculando)
                    numero = calculando
                
    else:
        while True:
                if numero == 1 or numero == 0:
                    calculando = numero
                    resultado.append(calculando)
                    print(calculando)
                    numero = calculando
                    break
                else:
                    calculando = numero*3+1
                    resultado.append(calculando)
                    print(calculando)
                    numero = calculando

serie_collatz()

   
