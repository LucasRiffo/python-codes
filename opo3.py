#CALCULAR PROMEDIO DE 3 EDADES
#CALCULAR PROMEDIO DE 3 NOTAS
#CALCULAR PROMEDIO DE 3 MESADAS

def promedio (a, b, c):
    return (a + b + c)/3

print(" *** Bienvenido *** ")
print("")

print("---| ALUMNO N°1 |----")

nombre1 = str(input("Ingrese nombre del alumno 1: "))
edad1 = int(input("Ingrese edad del alumno 1: "))
n1 = float(input("Ingrese nota del alumno 1: "))
mesada1 = int(input("Ingrese mesada del alumno 1: "))

print("")

print("---| ALUMNO N°2 |----")

nombre2 = str(input("Ingrese nombre del alumno 2: "))
edad2 = int(input("Ingrese edad del alumno 2: "))
n2 = float(input("Ingrese nota del alumno 2: "))
mesada2 = int(input("Ingrese mesada del alumno 2: "))

print("")

print("---| ALUMNO N°3 |----")

nombre3 = str(input("Ingrese nombre del alumno 3: "))
edad3 = int(input("Ingrese edad del alumno 3: "))
n3= float(input("Ingrese nota del alumno  3: "))
mesada3 = int(input("Ingrese mesada del alumno 3: "))

print(" *** Resultados *** ")

proe = promedio(edad1, edad2, edad3)
print ("")
print ("> El promedio de las edades es: ", proe)

pro = promedio(n1, n2, n3)
print ("")
print ("> El promedio de las notas es: ", pro)

prom  = promedio(mesada1, mesada2, mesada3) 
print ("")
print ("> El promedio de las mesadas es: ", prom)
