# Definição: Recursão é um método para resolver problemas que envolve quebrar o problema em subproblemas cada vez menores até atingir um problema simples o bastante que possa ser resolvido trivialmente.
#           Em geral a recursão envolve uma função que chama uma função.

# Três Leis da Recursão:
#   - Um algoritmo deve possuir um caso base:
#   - Um algoritmo deve modificar o seu estado e se aproximar do caso base
#   - Um algoritmo recursivo deve chamar a si mesmo, recusrivamente.


def find_max(numeros):
    if len(numeros)  == 1:
        return numeros[0]
    else:
        if numeros[0] >= numeros[1]:
            return find_max([numeros[0]] + numeros[2:])
        else:
            return find_max(numeros[1:])

print(find_max([5, 1]))
        