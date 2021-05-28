import os
os.system('cls')
print('\n\tEjercicio 2 LISTAS')
print('\tPrograma que crea una lista e inicializa con 5 cadenas de caracteres leídas por teclado.')
print('\tCopia los elementos de la lista en otra lista pero en orden inverso,')
print('\ty muestra sus elementos en pantalla.')
#inicializar variables
i = 1
lista = [] #Inicializa una LISTA VACÍA
#ciclo para pedir los elementos de la lista y compararlos
while i <= 5:
    elemento = str( input('\tIngrese Elemento: '))
    lista.append(elemento) #Agregamos el elemento a la lista
    i = i + 1
print ('\n\tElementos de tu lista: ', lista)
lista.reverse()
print ('\n\tEn orden invertido:',lista,'\n\n')
