def triangulo(x, tam):
    if tam == 1:
        print(' '*x + '+'*tam)
    else:
        triangulo(x+1, tam-2)
        print(' '*x + '+'*tam)
