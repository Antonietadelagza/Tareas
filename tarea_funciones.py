import os
os.system('cls')
#Declarar funciones
def mostrar_menú():
    print('\nPROGRAMA QUE CALCULA EL ÁREA DE LA FIGURA GEOMÉTRICA QUE ELIJA')
    print('\n\t\t\tMENÚ DE FIGURAS')
    print('\t\t\t1. CUADRADO')
    print('\t\t\t2. CÍRCULO')
    print('\t\t\t3. RECTÁNGULO')
    print('\t\t\t4. TRIÁNGULO')
    print('\t\t\t5. ROMBO')
    clave=int(input('\n\tELIGE EL NÚMERO DE LA FIGURA (1,2,3,4,5): '))
def a_cuadrado():
    print('\n\tPARA CALCULAR EL ÁREA DE UN CUADRADO')
    lado=float(input('\tTECLEA LA MEDIDA DE UN LADO : '))
    area = round((lado ** 2),2) 
    print ('\n\tEL ÁREA DEL CUADRADO ES: ',area,'\n')
def a_círculo():
    print('\n\tPARA CALCULAR EL ÁREA DE UN CÍRCULO')
    radio =float(input('\tTECLEA LA MEDIDA DEL RADIO : '))
    pi=3.1416
    area=round((pi*radio**2),2)
    print ('\n\tEL ÁREA DEL CÍRCULO ES: ',area,'\n')
def a_rectángulo():    
    print('\n\tPARA CALCULAR EL ÁREA DE UN RECTÁNGULO')
    base =float(input('\tTECLEA LA MEDIDA DE LA BASE : '))
    altura=float(input('\tTECLEA LA MEDIDA DE LA ALTURA: '))
    area=round((base*altura),2)
    print ('\n\tEL ÁREA DEL RECTÁNGULO ES: ',area,'\n')
def a_triángulo():
    print('\n\tPARA CALCULAR EL ÁREA DE UN TRIÁNGULO')
    base =float(input('\tTECLEA LA MEDIDA DE LA BASE : '))
    altura=float(input('\tTECLEA LA MEDIDA DE LA ALTURA: '))
    area=round((base*altura/2),2)
    print ('\n\tEL ÁREA DEL TRIÁNGULO ES: ',area,'\n')
def a_rombo():
    print('\n\tPARA CALCULAR EL ÁREA DE UN ROMBO')
    dmayor =float(input('\tTECLEA LA MEDIDA DE LA DIAGONAL MAYOR : '))
    dmenor=float(input('\tTECLEA LA MEDIDA DE LA DIAGONAL MENOR: '))
    area=round((dmayor*dmenor/2),2)
    print ('\n\tEL ÁREA DEL ROMBO ES: ',area,'\n')
def error():
    print('\n\t ¡ERROR! LA OPCIÓN NO ES VÁLIDA \n', '\t\t ELIJE SOLO 1,2,3,4,5) ')
    print('\n\t EJECUTA NUEVAMENTE EL PROGRAMA\n\n ')
#inicia programa
mostrar_menú()
if (clave==1):
    a_cuadrado()
elif (clave==2):
    a_círculo()
elif (clave==3):
    a_rectángulo()
elif (clave==4):
    a_triángulo()
elif (clave==5):
    a_rombo()
else:
    error()   