# Almacenar en un vector los numero 5,3,7,2,6,3
# Craer un codigo que ordene de menor a mayor

numeros = [5,3,7,2,6,3]

for i in range(1,len(numeros)):
    for j in range(len(numeros) - i):
        if numeros[j] > numeros[j+1]:
            aux = numeros[j]
            numeros[j] = numeros[j+1]
            numeros[j+1] = aux
print(numeros)

input()