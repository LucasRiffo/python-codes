#Ingresar datos de tres alumnos:
#Nombre
#Edad
#Nota
#Mesada
#Promediar edad, nota y mesada

nombre = [0,0,0]
especialidad = [0,0,0]
nota = [0,0,0]
edad = [0,0,0]
mesada = [0,0,0]
genero = [0,0,0]





print("*** Bienvenido ***")
print("")

def promedio(a, b, c):
    prom = (a + b + c) / 3
    return prom

def edadd():
    while True:
        edad = int(input())
        if 10 <= edad <= 20:
            return edad
        else:
            print("Edad no válida, ingrese una edad entre 10 y 20:")

def notaa():
    while True:
        nota = float(input())
        if 1 <= nota <= 7:
            return nota
        else:
            print("Nota no válida, ingrese una nota entre 1 y 7:")

def mesadaa():
    while True:
        mesada = input("Ingrese mesada (número entero): ")
        if mesada.isdigit():
            return int(mesada)
        else:
            print("Ingrese un número entero para la mesada: ")

def especialidadd():
    while True:
        print("Ingrese especialidad ([1] para Programacion, [2] Administracion, [3] Contabilidad): ")
        opcion = input()
        if opcion == '1' or opcion == '2' or opcion == '3':
            return int(opcion)
        else:
            print("Especialidad no valida, Ingrese [1] para Programaciom, [2] para Administracion, [3] para Contabilidad")

def generoo():
    while True:
        print("Ingrese genero del alumno ([1] para hombre, [2] para mujer): ")
        opcion = input()
        if opcion == '1' or opcion == '2':
            return int(opcion)
        else:
            print("Genero no valido, Ingrese [1] para hombre, [2] para mujer")

for i in range (3):
    print ("")
    print ("DATOS ALUMNO: ", i+1 )
    print ("")
    nombre[i] = input("Ingrese nombre del alumno: ")
    edad[i] = edadd()
    genero[i] = generoo()
    nota[i] = notaa()
    mesada[i] = mesadaa()
    especialidad[i] = especialidadd()


print("")
print("*** Respuestas ***")
print("")

promedio_edad = promedio(edad[0], edad[1], edad[2])
print("> El promedio de edad de los alumnos es: ", round(promedio_edad))

promedio_notas = promedio(nota[0], nota[1], nota[2])
print("> El promedio de las notas de los alumnos es: ", round(promedio_notas))

promedio_mesada = promedio(mesada[0], mesada[1], mesada[2])
print("> El promedio de las mesadas de los alumnos es: ")