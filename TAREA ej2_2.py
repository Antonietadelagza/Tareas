import os
os.system('cls')
print('\n\tEjercicio2')
print('\tPrograma que pida al usuario su peso (en kg) y estatura (en metros)')
print('\tcalcule el índice de masa corporal y lo almacene en una variable, y muestre en')
print('\tpantalla la frase: "Tu índice de masa corporal es <imc> donde <imc> es el índice')
print('\tde masa corporal calculado\n')
kilos = input('\n\t¿Cuál es tu peso en kg? ')
metros = input('\t¿Cuál es tu estatura en metros? ')
imc = round(float(kilos)/float(metros)**2,2)
print('\n\tTu índice de masa corporal es: ', imc) 
if (imc>18.5 and imc<24.9):
    print ('\n\tEstas en un rango normal, tienes peso saludable\n\n')
else:
    print ('\n\tEstas en un rango con sobrepeso, tienes obesidad.\n\n')
