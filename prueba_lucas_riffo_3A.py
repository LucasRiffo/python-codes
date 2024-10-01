print("*** Bienvenido ***")
print("")

ventas = int(input("Ingrese la cantidad de ventas que se realizarán: "))

def resta(a, b):
    return a - b

if ventas <= 0:
    print("La cantidad de ventas debe ser un número entero positivo.")
else:
    for i in range(ventas):
        print("*** COMPRADOR ", i + 1, " ***")
        nombre = input("Ingrese nombre del comprador: ")
        apellido = input("Ingrese apellido del comprador: ")
        nombreV = input("Ingrese nombre del vendedor: ")
        apellidoV = input("Ingrese apellido del vendedor: ")
        fruto = input("Fruta o Verdura que comprará el cliente: ")
        peso = float(input("Peso de lo que va a comprar el cliente (en kilogramos): "))
        precio = float(input("Precio de la Fruta o Verdura por kilo: "))
        paga = float(input("Con cuánto paga el cliente: "))
        
        total = precio * peso
        vuelto = resta(paga, total)
        
        print("")
        print("TOTAL A PAGAR: $", round(total, 2))
        print("VUELTO: $", round(vuelto, 2))
        print ("NOMBRE DEL COMPRADOR: ", nombre, apellido)
        print ("")