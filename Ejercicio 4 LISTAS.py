import os
os.system('cls')
print('\n\tEjercicio 4 LISTAS')
print('\tPrograma que declare una lista y la vaya llenando de números hasta que')
print('\tse introduzca un número negativo. Entonces se debe imprimir el vector')
print('\t(sólo los elementos introducidos).')
#inicializar variables
i = 1
lista = [] #Inicializa una LISTA VACÍA
#ciclo para pedir los elementos de la lista 
while True:
    elemento = int( input('\tIngresa un número: '))
    if elemento>=0:
        lista.append(elemento) #Agregamos el elemento a la lista
    elif elemento<0:
        print('\n\tIngresaste un número negativo, fin del bucle.')
        print('\n\tLos elementos de tu lista fueron: ', lista)
        print('\n')
        break