"""
def suma():
    numero_uno = int(input('Ingresa el primer número entero '))
    numero_dos = int(input('Ingresa el segundo número entero '))

    resultado = numero_uno + numero_dos
    print(resultado)

suma()
"""

"""
def suma(n1, n2):
    
    resultado = n1 + n2
    print(resultado)

numero_uno = int(input('Ingresa el primer número entero '))
numero_dos = int(input('Ingresa el segundo número entero '))

suma(numero_uno, numero_dos)
"""

def suma(n1, n2):
    
    return n1 + n2, 'La función retorna 2 valores'

numero_uno = int(input('Ingresa el primer número entero '))
numero_dos = int(input('Ingresa el segundo número entero '))

resultado, _ = suma(numero_uno, numero_dos)
print('El resultado es:', resultado)