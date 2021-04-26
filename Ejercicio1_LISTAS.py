import os
os.system('cls')
import random
print ('\n\t Ejercicio 1 LISTAS')    
print ('\n\t Programa que inicialice una lista con 10 valores aleatorios (del 1 al 10)')
print ('\t que muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.\n')
print ('\n\t\t\t\tNUMERO..CUADRADO..CUBO')
lista = (1,2,3,4,5,6,7,8,9,10)
aleatorio = random.sample(lista, 10)
for x in aleatorio:
    print ('\t\t\t\t',x,'\t', x**2,'\t', x**3 )