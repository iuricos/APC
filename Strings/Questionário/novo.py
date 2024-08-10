n = int(input())

for i in range(n):
    aux = input()
    caractere = aux[i]
    numero = ""
    while caractere.isdigit():
        numero += 1
        i += 1
    print(numero)
    

        
    
        






'''verifica se o caractere
é letra, caso seja, guarde
se não, concatene o dígi
to a uma string que armazena
números. enquanto percorre a string,
armazene o caractere vezes 
o número e adicione ao resultado
faça isso somente a quantidade len(a8x)
vezes'''