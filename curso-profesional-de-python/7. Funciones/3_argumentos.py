"""
def promedio(*args):
    print(args)
    print(type(args))
    return sum(args) / len(args)

resultado = promedio(10, 10, 5, 7, 10)
print(resultado)
"""
def promedio(*args):
    return sum(args) / len(args)


def combinacion(p1, p2, *args, p4=500):
    print(p1)
    print(p2)
    print(args)
    print(p4)

combinacion(10, 20, 1, 2, 3, 4, 5, 6, 7, 8, p4=1000)