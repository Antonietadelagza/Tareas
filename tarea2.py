print('\nPROGRAMA QUE CALCULA EL ÁREA DE UNA FIGURA GEOMÉTRICA QUE SE ELIJA')
print('\n\t\t\tMENÚ DE FIGURAS')
print('\t\t\t1. CUADRADO')
print('\t\t\t2. CÍRCULO')
print('\t\t\t3. RECTÁNGULO')
print('\t\t\t4. TRIÁNGULO')
print('\t\t\t5. ROMBO')
clave=int(input('\n\tELIGE EL NÚMERO DE UNA FIGURA (1,2,3,4,5): '))
if (clave==1):
    print('\n\tPARA CALCULAR EL ÁREA DE UN CUADRADO')
    lado=float(input('\tTECLEA LA MEDIDA DE UN LADO : '))
    area = lado ** 2 
    print ('\n\tEL ÁREA DEL CUADRADO ES: ',area,'\n')
elif (clave==2):
    print('\n\tPARA CALCULAR EL ÁREA DE UN CÍRCULO')
    radio =float(input('\tTECLEA LA MEDIDA DEL RADIO : '))
    pi=3.1416
    area=pi*radio**2
    print ('\n\tEL ÁREA DEL CÍRCULO ES: ',area,'\n')
elif (clave==3):
    print('\n\tPARA CALCULAR EL ÁREA DE UN RECTÁNGULO')
    base =float(input('\tTECLEA LA MEDIDA DE LA BASE : '))
    altura=float(input('\tTECLEA LA MEDIDA DE LA ALTURA: '))
    area=base*altura
    print ('\n\tEL ÁREA DEL RECTÁNGULO ES: ',area,'\n')
elif (clave==4):
    print('\n\tPARA CALCULAR EL ÁREA DE UN TRIÁNGULO')
    base =float(input('\tTECLEA LA MEDIDA DE LA BASE : '))
    altura=float(input('\tTECLEA LA MEDIDA DE LA ALTURA: '))
    area=base*altura/2
    print ('\n\tEL ÁREA DEL TRIÁNGULO ES: ',area,'\n')
elif (clave==5):
    print('\n\tPARA CALCULAR EL ÁREA DE UN ROMBO')
    dmayor =float(input('\tTECLEA LA MEDIDA DE LA DIAGONAL MAYOR : '))
    dmenor=float(input('\tTECLEA LA MEDIDA DE LA DIAGONAL MENOR: '))
    area=dmayor*dmenor/2
    print ('\n\tEL ÁREA DEL ROMBO ES: ',area,'\n')
elif (clave<=1 and clave>=5):
    print('\n\ ERROR. NÚMERO NO VÁLIDO. ELIJE SOLO 1,2,3,4,5) ')
    print('\t EJECUTA NUEVAMENTE EL PROGRAMA')