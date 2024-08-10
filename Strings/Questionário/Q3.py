n = int(input())

for char in range(n):
    aux = input()
    numero = ""
    caractere = ""
    i = 0
    resultado = ""

    while i < len(aux):
        caractere = aux[i]
        i += 1

        while caractere.isdigit():
            numero = numero + caractere
        
        if numero:
            resultado = caractere * (int(numero))
    print(resultado)