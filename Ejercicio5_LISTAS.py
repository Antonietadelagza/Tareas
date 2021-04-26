import os
os.system('cls')
print('\n\t EJERCICIO 5 LISTAS')
print('\t Programa que inicialice una lista de números con valores aleatorios...')
print('\t(10 valores), y posterior ordene los elementos de menor a mayor')
#inicializar variables
i = 1
mayor=0
Lista = [] #Inicializa una LISTA VACÍA
#ciclo para pedir los elementos de la lista y compararlos
while i <= 10:
    elemento = int( input('\tIngrese Elemento: '))
    Lista.append(elemento) #Agregamos el elemento a la lista
    i = i + 1
#Resultado
print('\n\tElementos de tu lista ')
print('\t',Lista)
Ordenada=sorted(Lista) # ordena los elementos en una nueva lista
print('\n\t Elementos ordenados de menor a mayor')
print('\t',Ordenada)

