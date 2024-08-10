n = int(input())


for _ in range(n):
    aux = input()

    resultado = ""
    i = 0
    comprimento = len(aux)
    
    while i < comprimento:
        caractere = aux[i]
        i += 1

        numero = ""
        while i < comprimento and aux[i].isdigit():
            numero += aux[i]
            i += 1
        
        # Adiciona a repetição ao resultado
        if numero:
            resultado += caractere * int(numero)
    
    # Imprime o resultado decodificado
    print(resultado)
