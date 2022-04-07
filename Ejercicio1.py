#Codigo que determina si un numero es primo o no

numero = int(input("Ingresa un numero: "))
primo = True
    
for n in range(2, numero):
    if numero % n == 0:
        primo = False
        break

if primo:
    print("El numero es primo")
else:
    print("El numero no es primo")

input()