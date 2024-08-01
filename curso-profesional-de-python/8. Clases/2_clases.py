# Attrs de clase
# Attrs de instancia

class Usuario:
    # Attrs de clase
    username = 'Username por default'
    email = ''

Usuario.username = 'User1'
Usuario.email = 'info@codigofacilito.com'

print(Usuario.username)
print(Usuario.email)
