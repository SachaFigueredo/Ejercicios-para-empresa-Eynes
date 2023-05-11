import random

# Función para crear una matriz 5x5 de números aleatorios
def crear_matriz():
    matriz = []
    for i in range(5):
        fila = []
        for j in range(5):
            fila.append(random.randint(0, 9))
        matriz.append(fila)
    return matriz

# Función para buscar una secuencia de 4 números consecutivos en una fila
def buscar_secuencia_horizontal(fila):
    for i in range(len(fila)-3):
        if fila[i] == fila[i+1] == fila[i+2] == fila[i+3]:
            return (i, i+3)
    return None

# Función para buscar una secuencia de 4 números consecutivos en una columna
def buscar_secuencia_vertical(matriz, col):
    for i in range(len(matriz)-3):
        if matriz[i][col] == matriz[i+1][col] == matriz[i+2][col] == matriz[i+3][col]:
            return (i, i+3)
    return None

# Función para buscar una secuencia de 4 números consecutivos en la matriz
def buscar_secuencia(matriz):
    for i in range(5):
        secuencia_horizontal = buscar_secuencia_horizontal(matriz[i])
        if secuencia_horizontal:
            return ((i, secuencia_horizontal[0]), (i, secuencia_horizontal[1]))
    for j in range(5):
        secuencia_vertical = buscar_secuencia_vertical(matriz, j)
        if secuencia_vertical:
            return ((secuencia_vertical[0], j), (secuencia_vertical[1], j))
    return None

# Ejemplo de uso
matriz = crear_matriz()
print("Matriz generada:")
for fila in matriz:
    print(fila)
secuencia = buscar_secuencia(matriz)
if secuencia: 
    print(f"Se encontró una secuencia de 4 números consecutivos entre las posiciones {secuencia[0]} y {secuencia[1]}")
else:
    print("No se encontró ninguna secuencia de 4 números consecutivos")
