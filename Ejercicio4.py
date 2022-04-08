# Almacenar en un arreglo los numeros: 5,4,7,2,8,4,6
# Obtener media, desviacion estandar y varianza
#numeros = [5,4,7,2,8,4,6]
numeros = [8.5,7.0,9.5,8.0,9.0,8.8,7.5,10]
suma = 0
cont = 0
varianza = 0
sumVar = 0
prom = 0

sumVarianza = 0

for num in numeros:
    suma = suma + num
    cont = cont + 1
prom = suma / cont

for num in numeros:
    varianza = (num - prom)
    varianza = varianza ** 2
    sumVarianza = sumVarianza + varianza
varianza = sumVarianza / cont



print("La media del vector es: ", suma / cont)
print("La desviacion estandar del vector es: ", pow(varianza,2))
print("La varianza del vector es: ", varianza)  


