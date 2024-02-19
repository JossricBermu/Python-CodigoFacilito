lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

# Ordena la lista de menor a mayor
lista.sort()

# Ordena la lista de mayor a menor
lista.sort(reverse=True)

print(lista)

print(min(lista)) # número min
print(max(lista)) # número max

# Comprobar si un elemento existe dentro de la lista
print(10 in lista)
print(11 not in lista)