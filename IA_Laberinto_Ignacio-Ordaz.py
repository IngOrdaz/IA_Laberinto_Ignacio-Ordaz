"""
    Introducción a la Inteligencia Artificial: El papelde la heurística
    Ignacio Alejandro Ordaz Estrada
    N.C. 17120188
"""

#VARIABLES
#---------------------------------------------------------------------------#
#contador para la impresion del laberinto
m=0
#matriz 9X9 que se utilizará (es la que está en el PDF)
laberinto = [ 
    ['1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['O', ' ', ' ', ' ', ' ', ' ', '1', ' ', '1'],
    ['1', '1', '1', ' ', '1', '1', '1', ' ', '1'],
    ['1', ' ', ' ', ' ', '1', ' ', '1', ' ', '1'],
    ['1', ' ', '1', '1', '1', ' ', '1', ' ', '1'],
    ['1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1'],
    ['1', ' ', '1', '1', '1', ' ', '1', ' ', '1'],
    ['X', ' ', '1', ' ', ' ', ' ', '1', ' ', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1']
]
"""
#-- solo los uso para pobrar impresiones del punto inicial y final que yo estableci
print(laberinto[1][0])
print(laberinto[7][0])
"""

#variables para recorrer la matriz
fila=1
columna=0

#FUNCIONES
#---------------------------------------------------------------------------#

#función para imprimir el laberito inicial y resuelto
def mostrar_laberinto(laberinto):
    if(m==0):
        print("Laberinto inicial")
        for fila in laberinto:
            for columna in fila:
                print(columna, end=' ')
            print(" ")
    
    elif(m==1):
        print("Laberinto final")
        for fila in laberinto:
            for columna in fila:
                print(columna, end=' ')
            print(" ")

#funcion para resolver el laberinto
def resolver(laberinto, fila, columna):
    
    # si estamos en el inicio agregamos el caracter '-' a la matriz y devolvemos true
    if laberinto[fila][columna] == 'X':
        laberinto[fila][columna]='-'
        return True

    # Si la posición actual es pared o ya pasamos por ahi, devolvemos False
    if laberinto[fila][columna] == '1' or laberinto[fila][columna] == 'v':
        return False

    # cambiamos el valor por una 'v' de visitado
    laberinto[fila][columna] = 'v'

    # comprobar si podemos avanzar hacaia algun punto (arriba, derecha, abajo, izquierda)
    if ((fila > 0 and resolver(laberinto, fila - 1, columna)) or 
        (columna < len(laberinto[fila]) - 1 and resolver(laberinto, fila, columna + 1)) or 
        (fila < len(laberinto) - 1 and resolver(laberinto, fila + 1, columna)) or 
        (columna > 0 and resolver(laberinto, fila, columna - 1))):
        # Si pudimos avanzar modificamos con el carcater '-' de que por ahi va el camino
        laberinto[fila][columna]='-'
        return True

    # Si no se puede avanzar la dejamos vacia 
    laberinto[fila][columna] = ' '
    
    return False

#MAIN
#imprimo primer laberinto
mostrar_laberinto(laberinto)
#llamo metodo para resolverlo
resolver(laberinto,fila,columna)
m=1
#imprimo laberinto resuelto
mostrar_laberinto(laberinto)
