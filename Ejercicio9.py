#Generar 300 numeros aleatorios en un rango de 500 a 1000
# guardar los numeros en un arreglo
#Determinar mayor, menor, media, desviacion estandar y media

import random
import math

arreglo = []
numero = 0
media = 0
suma = 0
cont = 0
varianza = 0
sumVarianza = 0

for i in range(300):
    numero = random.randint(500,1000)
    arreglo.append(numero)

mayor = arreglo[0]
for num in arreglo:

    if(num > mayor):
        mayor = num

menor = arreglo[0]
for num in arreglo:
    if num < menor:
        menor = num

for num in arreglo:
    suma = suma + num
    cont = cont + 1
media = suma / cont

for num in arreglo:
    varianza = (num - media)
    varianza = varianza ** 2
    sumVarianza = sumVarianza + varianza

varianza = sumVarianza / cont


print("El numero mayor es: ", mayor)
print("El numero menor es: ", menor)
print("La media es: ", media)
print("La varianza es: ", varianza)
print("La desviacion estandar es: ", math.sqrt(varianza))

input()