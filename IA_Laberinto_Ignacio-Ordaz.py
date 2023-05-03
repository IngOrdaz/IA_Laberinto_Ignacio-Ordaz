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

def resolver(laberinto, fila, columna):
    # Caso base: si estamos en la meta, añadir la posición actual al camino y devolver True
    if laberinto[fila][columna] == 'X':
        laberinto[fila][columna]='-'
        return True

    # Si la posición actual es un muro o ya la visitamos, devolver False
    if laberinto[fila][columna] == '1' or laberinto[fila][columna] == '.':
        return False

    # Marcar la posición actual como visitada
    laberinto[fila][columna] = '.'

    # Verificar si podemos avanzar en alguna dirección (arriba, derecha, abajo, izquierda)
    if ((fila > 0 and resolver(laberinto, fila - 1, columna)) or 
        (columna < len(laberinto[fila]) - 1 and resolver(laberinto, fila, columna + 1)) or 
        (fila < len(laberinto) - 1 and resolver(laberinto, fila + 1, columna)) or 
        (columna > 0 and resolver(laberinto, fila, columna - 1))):
        # Si pudimos avanzar en alguna dirección, añadir la posición actual al camino
        laberinto[fila][columna]='-'
        return True

    # Si no pudimos avanzar en ninguna dirección, desmarcar la posición actual y devolver False
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