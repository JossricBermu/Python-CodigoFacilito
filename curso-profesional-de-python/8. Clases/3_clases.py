# Attrs de clase
# Attrs de instancia

class Usuario:
    # Attrs de clase
    username = 'Username por default'
    email = ''

# __dict__

user1 = Usuario()
# 1.- Verifica si el attr xisten dentro del objeto
# 2.- Verifica si el attr existe dentro de la clase -> Lectura
# 3.- Lanza un error
print(user1.username)

print(id(user1.username))
print(id(Usuario.username))

print(user1.__dict__) # Dict
