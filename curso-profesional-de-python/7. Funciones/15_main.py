def pares(): # Generador -> Lazy iterator
    for numero in range(0, 12, 2):
        yield numero # La función suspende su ejecución

        print('Se reanuda la ejecución')

generador = pares()

while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print('El generador finalizo.')
        break