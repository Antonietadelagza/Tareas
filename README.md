# Tareasimport os
os.system('cls')
print('Programa que calcula la fecha de tu naciemiento')
nombre= str(input('\n\t\tDime tu nombre:'))
edad= int(input('\n\t\tDime tu edad:'))
while (edad<=0 or edad>100):
    print('ESA EDAD NO ES VÁLIDA')
    os.system('cls')
    edad= int(input('\n\t\tDime tu edad:'))
else:
    fecha= str(input('\n\t¿en qué fecha cumples años (día y mes):'))
    year=2021-edad
os.system('cls')
print('\n\',nombre,' TU FECHA DE NACIMIENTO ES: ',fecha, year)   
