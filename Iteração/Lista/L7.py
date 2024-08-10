def ehPrimo(x):
    contador = 0
    for i in range(1, x):
        if x % i == 0:
            contador += 1
    if contador == 1 :
        return 1
    else:
        return 0

def divisoresPrimos(x):
    contador = 0

    for i in range(1, x):
        if x % i == 0:
            if ehPrimo(i) == 1:
                contador += 1
    return contador
        