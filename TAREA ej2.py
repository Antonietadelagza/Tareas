import os
os.system('cls')
print('\n\tEjercicio2')
print('\nPrograma que almacena en una lista los siguientes precios, 50, 75, 46,')
print('\n22, 80, 65, 8, y muestra por pantalla el menor y el mayor de los precios.')
precio = [50, 75, 46, 22, 80, 65, 8,] #Inicializa la LISTA 
mayor=0
# busca el precio mayor
for x in range(1,7):
    if precio[x]>mayor:
        mayor=precio[x]
# busca la calificación menor
menor=precio[0]
for x in range(1,7):
    if precio[x]<menor:
        menor=precio[x]
#Resultado
print('\n\tLista de precios: ', precio)
print('\n\tEl precio mayor es: ', mayor)
print('\n\tEl precio menor es: ', menor)
print('\n\n')