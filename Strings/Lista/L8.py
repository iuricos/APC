n = int(input())

for i in range(n):
    aux = input()

    resultado = ""
    c = 0
    comprimento = len(aux)
    
    while c < comprimento:
        caractere = aux[c]
        c += 1

        numero = ""
        while c < comprimento and aux[c].isdigit():
            numero += aux[c]
            c += 1

        resultado += caractere * int(numero)
    

    print(resultado)

