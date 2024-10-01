def promedio_curso(n1,n2,n3,n4,n5):
    prom = 0
    prom = (n1+n2+n3+n4+n5)/5
    return prom

def promedio_notas(n1,n2,n3,p1,p2,p3):
    prom = 0
    prom = (p1*n1+p2*n2+p3*n3)/100
    return prom
#nota 1= 20%, nota 2= 30%, nota 3= 50%
p1=20
p2=30
p3=50

apellido = [0,0,0,0,0]
nombre = [0,0,0,0,0]
nota1 = [0,0,0,0,0]
nota2 = [0,0,0,0,0]
nota3 = [0,0,0,0,0]
prom = [0,0,0,0,0]

print("*** Bienvenido ***")
print("")

for i in range(0,5,1):
    # x = i + 1
    nombre[i] = str(input(f"Ingrese nombre del Alumno {i+1}: "))
    apellido[i] = str(input(f"Ingrese apellido del Alumno {i+1}: "))
    print("")
    nota1[i] = float(input("> Ingrese la primera nota: "))
    nota2[i] = float(input("> Ingrese la segunda nota: "))
    nota3[i] = float(input("> Ingrese la tercera nota: "))
    prom[i] = promedio_notas(nota1[i],nota2[i],nota3[i],p1,p2,p3)
    print("El promedio del alumno es: ", prom[i])
    print("")


print("")
promtotal = promedio_curso(prom[0],prom[1],prom[2],prom[3],prom[4])
print("> El promedio TOTAL del curso es: ", promtotal)

# Imprimir todas las notas por alumno
i == 0
print("*** RESULTADOS ***")
print("")

for i in range(0,5,1):
    print(f"> Alumno {i+1}: {nombre[i]} {apellido[i]}")
    print("> NOTA 1 =", nota1[i])
    print("> NOTA 2 =", nota2[i])
    print("> NOTA 3 =", nota3[i])
    print("> PROMEDIO = ", prom[i])
    print("")
    
