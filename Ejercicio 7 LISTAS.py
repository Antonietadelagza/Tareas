import os
os.system('cls')
print('\n\t\tEjercicio 7 LISTAS')
print('\t\tPrograma que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’')
print('\t\tde cinco enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ ')
print('\t\ty calcule lista3=lista1+lista2.\n\n')
#Inicializa LISTAS VACÍAS
i=1
n=1
#x=1
lista1 = [] 
lista2 = [] 
lista3 = [] 
#ciclo para pedir los elementos de la lista1 
print('\t\tPara completar la lista1\n')
while i <= 5:
    elemento = int( input('\tIngrese un número: '))
    lista1.append(elemento) #Agregamos el elemento a la lista
    i = i + 1
#ciclo para pedir los elementos de la lista2 
print('\n\t\tPara completar la lista2')
while n <= 5:
    elemento = int( input('\tIngrese un número: '))
    lista2.append(elemento) #Agregamos el elemento a la lista
    n = n + 1
#ciclo para sumar elementos de las dos listas
for x, w in enumerate(lista1):
    lista3.append(lista1[x] + lista2[x])
print('\n\t\t\tLista1: ',lista1)
print('\n\t\t\tLista2: ',lista2)
print('\n\t\t\tLista3: ',lista3)

