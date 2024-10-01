print("*** Bienvenido ***")
print("")

artistas = int(input("Ingrese número de artistas: "))
print("")

fecha = [0] * artistas
nombre = [0] * artistas
apellido = [0] * artistas
apodo = [0] * artistas
sueldo = [0] * artistas

for i in range(artistas):
    apodo[i] = input(f"Ingrese apodo del Artista {i + 1}: ")
    nombre[i] = input("Ingrese nombre del Artista: ")
    apellido[i] = input("Ingrese apellido del Artista: ")

    while True:
        sueldo[i] = int(input("Ingrese sueldo del Artista (desde $1.000.000 hasta $17.000.000): $"))
        if 1000000 <= sueldo[i] <= 17000000:
            break
        print("Monto Incorrecto. Intente de nuevo.")
        print("")

    while True:
        fecha[i] = int(input("Ingrese día que presenta (17, 18, 19 o 20 de Sep): "))
        if fecha[i] in [17, 18, 19, 20]:
            break
        print("Fecha Incorrecta, intente de nuevo.")
        print("")

print("*** Lista de Artistas ***")
for i in range(artistas):
    print("")
    print(f"> Artista: |{apodo[i]}| ")
    print(f"> Nombre: {nombre[i]}")
    print(f"> Apellido: {apellido[i]}")
    print(f"> Sueldo: ${sueldo[i]}")
    print(f"> Fecha que presenta: {fecha[i]} de Septiembre")

promedio_sueldo = sum(sueldo) / artistas
max_sueldo_index = sueldo.index(max(sueldo))
artista_mas_pagado = f"{apodo[max_sueldo_index]} con sueldo de ${sueldo[max_sueldo_index]}"

print("")
print("*** RESULTADOS ***")
print("")
print(f"El promedio de sueldos de los artistas es: ${promedio_sueldo:.2f}")
print(f"El artista más pagado es: {artista_mas_pagado}")