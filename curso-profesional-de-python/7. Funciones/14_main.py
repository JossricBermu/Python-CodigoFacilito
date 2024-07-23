def pares(): # Generador -> Lazy iterator
    for numero in range(0, 100, 2):
        yield numero # La función suspende su ejecución

        print('Se reanuda la ejecución')

for par in pares():
    print(par)
