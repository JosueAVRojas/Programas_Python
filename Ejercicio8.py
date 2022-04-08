#Generar 300 numeros aleatorios en un rango de 500 a 1000
# guardar los numeros en un arreglo
import random

arreglo = []
numero = 0

for i in range(300):
    numero = random.randint(500,1000)
    arreglo.append(numero)

print(arreglo)

input()