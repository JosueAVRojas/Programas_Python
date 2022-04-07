# Almacenar en un vector los numero 5,3,7,2,6,3
# Determinar el numero mayor

numeros = [5,3,7,2,6,3]
mayor = numeros[0]

for num in numeros:

    if(num > mayor):
        mayor = num
        print("El numero mayor es: ", mayor)

input()