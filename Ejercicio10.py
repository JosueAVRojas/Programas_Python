#Juego de los datos usando la libreria random

import random

numero = random.randint(1, 10)

while numero % 2 == 0:
    print(numero)
    numero = random.randint(1, 10)

if numero == 3:
    print("Ganaste el juego")
    print(numero)
else: 
    print("perdiste el juego")

input()