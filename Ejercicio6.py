# Obtener denominaciones de billete de un electrodomestico de precio 5560

cantidad = 5560
total = 0

denominaciones = [500, 200, 100, 50, 20]

for i in denominaciones:
    if cantidad >= i:
        total = cantidad // i
        print("Billetes de "+ str(i) + ": " + str(total))
        cantidad = cantidad % i
