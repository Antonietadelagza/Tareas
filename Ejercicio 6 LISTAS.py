import os
os.system('cls')
print('\n\tEjercicio 6 LISTAS')
print('\tPrograma que pida el número de mes y muestre el nombre del mes y cuántos días tiene.')
#inicializar listas
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'] 
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
opcion = int( input('\n\t\tIngresa el número de un mes: '))
if opcion>=1 and opcion<=12:
    print('\n\t\t',meses[opcion-1], ' tiene', dias[opcion-1], ' días','\n\n')
elif opcion<1 or opcion>12:
    print ('\n\t\tNúmero de mes incorrecto, elige entre 1 y 12')
    print ('\n\t\tEjecuta nuevamente el programa\n\n')
