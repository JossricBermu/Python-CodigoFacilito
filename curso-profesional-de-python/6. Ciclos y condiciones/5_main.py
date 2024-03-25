"""
variable = 'Cody' or 'CodigoFacilito'
variable = '' or 0 or [] or True
"""

listado = []
nombre = 'Cody'

"""
if listado:
    variable = listado
else:
    variable = nombre
"""

variable = listado or nombre

print(variable)