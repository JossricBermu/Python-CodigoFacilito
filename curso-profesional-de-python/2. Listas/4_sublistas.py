lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
#                  0         1         2        3      4        5

# [start:end]

sub_lista = lista_cursos[0:3]
print(sub_lista)

sub_lista = lista_cursos[1:4]
print(sub_lista)

# [start:] -> Obtenemos los últimos elementos de la lista
sub_lista = lista_cursos[3:]
print(sub_lista)

# [:end] -> Obtenemos los primeros elementos de la lista
sub_lista = lista_cursos[:4]
print(sub_lista)

# [start:end:skip]
sub_lista = lista_cursos[1:5:2]
print(sub_lista)

# lista invertida
sub_lista = lista_cursos[::-1]
print(sub_lista)