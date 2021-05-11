import os
os.system('cls')
print('\n\tEjercicio2')
print('\tPrograma que almacena la cadena de caracteres contraseña en un variable,')
print('\tpide al usuario la contraseña, y muestra en pantalla si lo ingresado coincide')
print('\tcon lo guardado, sin considerar mayúsculas ni minúculas\n\n')

variable = 'contraseña'
clave = input('\n\tTeclea la contraseña: ')
# Compara 
if variable == clave.lower():
    print('\n\tBIEN. La contaseña coincide\n\n')
else:
    print('\n\tLO SIENTO. La contraseña no coincide\n\n')
  