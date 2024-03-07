titulo_curso = 'Curso profesional de Python'

"""
contador = titulo_curso.count('a')

print(contador)
"""

print('Python' in titulo_curso.lower())
print('codigofacilito' not in titulo_curso.lower())

# Comprobar si un string se encuentra al inicio de un string base
print(titulo_curso.startswith('Curso'))

# Comprobar si un string se encuentra al final de un string base
print(titulo_curso.endswith('Python'))
