#Import random
import random

#Create the function below:
def matrixBuilder(filas, columnas):
    matrix=[]
    for _ in range(filas):
        fila=[valor]* filas
        matrix.append(fila)
    return matrix
filas=5
valor=1
malla= matrixBuilder(filas,valor)
for fila in malla:
    print(fila)
