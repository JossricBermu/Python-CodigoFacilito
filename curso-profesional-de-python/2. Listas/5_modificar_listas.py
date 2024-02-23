lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
lista_cursos_2 = ['C', 'C++', 'Docker']

print(len(lista_cursos))

# Agregar elementos al final de la lista
lista_cursos.append('MongoDB')
lista_cursos.append('C#')
lista_cursos.append('JavaScript')

# Añadir un elemento apartir de un índice
lista_cursos.insert(1, 'Rails')
lista_cursos.insert(0, 'Pygame')

# Extender una lista a partir de los elementos de otra lista
lista_cursos.extend(lista_cursos_2)

print(lista_cursos)
print(len(lista_cursos))

# Eliminar elementos de la lista
lista_cursos.remove('MongoDB')
# Eliminando elemento por el índice
del lista_cursos[0]

# Elimina todos los elementos de la  lista
lista_cursos.clear()

print(lista_cursos)
