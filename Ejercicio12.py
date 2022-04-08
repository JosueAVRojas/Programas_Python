#programa de tienda en python

producto= ["Jabon", "cepillo", "Shampoo", "toalla", "Cafe", "Jamon", "Queso", "Capsup", "Tomate", "Chicle"]
cantidad = [10,10,10,10,10,10,10,10,10,10]
precio = [15,20,13,55,12,24,35,35,79,34]
ventas = []

caja = 1000
suma = 0

salir = "s"

while salir == "s":

    print("1 - Venta")
    print("2 - Consultar Inventario")
    print("3 - Agregar Inventario")
    print("4 - Corte de caja")  
    print("5 - Salir") 


    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        ven = int(input("Selecciona el producto a vender: "))
        ven = ven -1

        for x in range(len(producto)):
            if ven == x:
                print("Produto: ",producto[x], ", Cantidad: ",cantidad[x], ", Precio: ",precio[x])

                cantidadVenta = int(input("Ingresa la cantidad de producto que desea: "))
                aux = cantidad[x]
                aux2 = precio[x]
                total = aux2 * cantidadVenta
                cantidadVenta = aux - cantidadVenta
                cantidad[x] = cantidadVenta

                ventas.extend([total])

    
    if opcion == "2":
        for x in range(len(producto)):
            print("Produto: ",producto[x], ", Cantidad: ",cantidad[x], ", Precio: ",precio[x])

    if opcion == "3":
        produc = input("Agrega el nombre del producto: ")
        cant = 10
        prec = input("Agrega el precio del producto: ")

        producto.extend([produc])
        cantidad.extend([cant])
        precio.extend([prec])

    if opcion == "4":
        print("ERealizando el corte de caja....")
        for x in ventas:
            suma = suma + x
        
        caja = caja + suma

        print("El corte de la caja fue un total de: ", caja)


    if opcion == "5":
        print("Saliendo del sistema..")
        break


    salir=input("Desea continuar?: s/n")