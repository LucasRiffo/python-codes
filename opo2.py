#Crear un programa que inrese 3 de notas para cada alumno
#Ingresar la cantidad de alumnos del curso
#Para cada alumno deve ingresar:
#Nombre
#Genero
#Notas (nota1, nota2, nota3)
#Calcular promedio para cada alumno
#Calcular cuantas mujeres hay en el curso
#Calcular el promedio de los hombres

def promedio (a, b, c):
    return (a + b + c)/3

contadormasculino = 0
contadormujer = 0
prom = 0
contalumno = 0
sumapromediohombres = 0

print (" *** Bienveindo *** ")
print ("")

alumnos = int(input("Ingrese la cantidad de alumnos: "))

for i in range(0, alumnos, 1):
    contalumno = contalumno+1
    nombre = str(input("Ingrese nombre del alumno: "))
    genero = int(input("Ingrese genero del alumno, *[1] para HOMBRE* y *[2] para MUJER*: "))
    n1 = float(input("Ingrese nota 1: "))
    n2 = float(input("Ingrese nota 2: "))
    n3 = float(input("Ingrese nota 3: "))

    pro = promedio(n1, n2, n3)
    print ("")
    print ("El promedio del alumno es: ", pro)

    if(genero=="2"): 
        contadormujer = contadormujer + 1
    else:
        contadormasculino = contadormasculino + 1 
        sumapromediohombres += pro

print ("")
print (" *** Resultados *** ")
print ("")
print ("La cantidad de mujeres es ", contadormujer)
print ("El promedio de los hombres es ", sumapromediohombres / contadormasculino)