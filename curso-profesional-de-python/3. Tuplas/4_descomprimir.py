numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# *nombre_variable -> almacena todos los valores restantes creando una lista
uno, dos, tres, cuatro, *resto_valores = numeros

print(uno)
print(dos)
print(tres)
print(cuatro)
print(resto_valores)

'''*_ -> Omitir el resto de valores, es decir la lista de
elementos restantes no me interesan, así que no las voy a
almacenar en una variable'''
uno, dos, tres, cuatro, *_ = numeros
print(uno)
print(dos)
print(tres)
print(cuatro)

uno, _, tres, cuatro, *_, nueve, diez = numeros
print(uno)
print(tres)
print(cuatro)
print(nueve)
print(diez)