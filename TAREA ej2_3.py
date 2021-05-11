import os
os.system('cls')
print('\n\tEjercicio2')
print('\tUna panadería vende barras de pan a 27 pesos cada una. El pan que no es el día')
print('\ttiene un descuento del 60%. Programa que pregunte el número de barras vendidas')
print('\tque no son del día. Después el programa debe mostrar el precio habitual de una barra')
print('\tde pan, el descuento que se le hace por no ser fresca y el total a pagar\n')
barras = int(input('\n\t¿Cuántas barras frías vendiste? '))
precio = 27 
descuento = 0.6
pago = barras * precio * (1 - descuento)
print('\n\tEl precio de una barra de pan fresca es: $', precio
print('\tEl descuento en una barra fría es: ', descuento*100, '%')
print("\tEl total a pagar es: $", round(pago,2)
 