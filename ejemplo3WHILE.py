import os
os.system('cls')
n=1
i=1
suma=0
print('PROGRAMA QUE CALCULA EL PROMEDIO DE UN GRUPO')
print('CON "n" ALUMNOS Y "N" CALIFICACIONES')
cant= int(input('\n\t¿CUÁNTOS ALUMNOS TIENE EL GRUPO?:'))
while (n<=cant):
    c= int(input('\n\t¿CUÁNTAS CALIFICACIONES A PROMEDIAR?: '))
    n=n+1
    while (i<=c):
        cal= float(input('\n\t\tCalificación:'))
        suma=suma+cal      
        i=i+1
else:
    prom=suma /c
    print ('\n\t\tEl promedio del alumno: ',n,' es: ',prom)
        
#else:
    print('TERMINAMOS')