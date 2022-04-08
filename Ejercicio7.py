# cambiar denominacion y cantidad

cantidad = 1570
total = 0

denominaciones = [200, 50, 20]

for i in denominaciones:
    if cantidad >= i:
        total = cantidad // i
        print("Billetes de "+ str(i) + ": " + str(total))
        cantidad = cantidad % i
