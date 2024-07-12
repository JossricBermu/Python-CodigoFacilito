"""
a -> La función principal (Decorador)
b -> La función de decorar
c -> La función decorada

a(b) -> c
"""

def funcion_a(funcion_b):

    def funcion_c():
        print('>>> Antes del llamado.')

        funcion_b()

        print('>>> Después del llamado.')

    return funcion_c

@funcion_a
def saludar():
    print('Hola, nos encontramos en una función')


@funcion_a
def suma():
    print(10 + 30)

suma()