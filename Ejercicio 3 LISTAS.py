import os
os.system('cls')
print('\n\tEjercicio 3 LISTAS')
print('\tPrograma que lea por teclado las 5 notas obtenidas por un alumno')
print('\t(comprendidas entre 0 y 10). Debe mostrar todas las notas, la nota media,')
print('\t la nota más alta que ha sacado y la menor.\n')
#inicializar variables
i = 1
suma=0
lista = [] #Inicializa una LISTA VACÍA
mayor=0
posicion=0
#ciclo para pedir los elementos de la lista y compararlos
while i <= 5:
    elemento = int( input('\tIngrese calificación: '))
    lista.append(elemento) #Agregamos el elemento a la lista
    suma=suma+elemento
    i = i + 1
# busca la calificación mayor
for x in range(1,5):
    if lista[x]>mayor:
        mayor=lista[x]
# busca la calificación menor
menor=lista[0]
for x in range(1,5):
    if lista[x]<menor:
        menor=lista[x]
#Resultado
print('\n\tCalificaciones del alumno: ', lista)
print('\n\t Promedio: ', suma/5)
print('\n\tCalificación mayor: ', mayor)
print('\n\tCalificación menor', menor)
print('\n\n')

