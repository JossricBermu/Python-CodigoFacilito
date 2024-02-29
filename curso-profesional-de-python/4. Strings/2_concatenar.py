nombre = 'Eduardo Ismael'
apellido = 'García'

# nombre_completo = 'Mr.' + nombre + ' ' + apellido + '.'

# nombre_completo = 'Mr. %s %s %s.' %(nombre, apellido, 'Pérez')

nombre_completo = 'Mr. {nombre} {primer_apellido} {segundo_apellido}.'.format(
    nombre = nombre,
    primer_apellido = apellido,
    segundo_apellido = 'Pérez'
)
print(nombre_completo)
