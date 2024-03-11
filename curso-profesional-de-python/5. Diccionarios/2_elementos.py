diccionario = {'a':1, 'b':2, 'c':3, 'd':4}

print('z' in diccionario)

"""
valor = diccionario['a']
print(valor)
"""

# get -> Obtener los valores de las llaves
valor = diccionario.get('e', None)
# setdefault -> Almacena una llave
valor = diccionario.setdefault('e', 5)
print(valor)
print(diccionario)