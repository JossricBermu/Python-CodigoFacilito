# Attrs de clase
# Attrs de instancia

class Usuario:
    # Attrs de clase
    username = 'Username por default'
    email = ''

# __dict__

user1 = Usuario()
user2 = Usuario()

# 1.- Verifica si el attr xisten dentro del objeto
# 2.- Verifica si el attr existe dentro de la clase -> Lectura
# 3.- Lanzará un error

user1.username = 'Cody' # Añadimos el attrs al objeto
user1.passeord = '1234'
print(user1.username) # De instancia

print(id(user1.username))
print(id(Usuario.username))

user1.password = 'password'

print(user1.__dict__) # Dict
