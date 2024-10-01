def promedio_curso(n1, n2, n3, n4, n5):
    prom = (n1 + n2 + n3 + n4 + n5) / 5
    return prom

def promedio_notas(n1, n2, n3, p1, p2, p3):
    prom = (p1 * n1 + p2 * n2 + p3 * n3) / 100
    return prom

p1 = 20
p2 = 30
p3 = 50

apellido = [0, 0, 0, 0, 0]
nombre = [0, 0, 0, 0, 0]
nota1 = [0, 0, 0, 0, 0]
nota2 = [0, 0, 0, 0, 0]
nota3 = [0, 0, 0, 0, 0]
prom = [0, 0, 0, 0, 0]
mejor_nota = [0, 0, 0, 0, 0]

print("*** Bienvenido ***")
print("")

for i in range(5):
    nombre[i] = str(input(f"Ingrese nombre del Alumno {i + 1}: "))
    apellido[i] = str(input(f"Ingrese apellido del Alumno {i + 1}: "))
    print("")

    while True:
        nota1[i] = float(input("> Ingrese la primera nota: "))
        if 1 < nota1[i] < 7.00001:
            break
        print("Nota inválida. NOTA MINIMA= 1, NOTA MAXIMA = 7")

    while True:
        nota2[i] = float(input("> Ingrese la segunda nota: "))
        if 1 < nota2[i] < 7.00001:
            break
        print("Nota inválida. NOTA MINIMA= 1, NOTA MAXIMA = 7")

    while True:
        nota3[i] = float(input("> Ingrese la tercera nota: "))
        if 1 < nota3[i] < 7.00001:
            break
        print("Nota inválida. NOTA MINIMA= 1, NOTA MAXIMA = 7")

    prom[i] = promedio_notas(nota1[i], nota2[i], nota3[i], p1, p2, p3)
    mejor_nota[i] = max(nota1[i], nota2[i], nota3[i]) 
    print("El promedio del alumno es: ", prom[i])
    print("La mejor nota del alumno es: ", mejor_nota[i])
    print("")

print("")
promtotal = promedio_curso(prom[0], prom[1], prom[2], prom[3], prom[4])
promedio_mas_alto = max(prom) 
print("> El promedio TOTAL del curso es: ", promtotal)
print("> El promedio más alto es: ", promedio_mas_alto)

print("*** RESULTADOS ***")
print("")

for i in range(5):
    print(f"> Alumno {i + 1}: {nombre[i]} {apellido[i]}")
    print("> NOTA 1 =", nota1[i])
    print("> NOTA 2 =", nota2[i])
    print("> NOTA 3 =", nota3[i])
    print("> PROMEDIO =", prom[i])
    print("> MEJOR NOTA =", mejor_nota[i])
    print("")
