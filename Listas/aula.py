'''
Tarefa de redução:
    normalmente não modifica a lista
    reduzir lista
Tarefa de Mapeamento:
    Gerar uma nova lista a partir dos valores de uma primeira
    listas "São alteradas" quando se define uma função para iterar siibre a lista

Filtragem:
    filtrar dados de uma lista


t = [[1, 2], [3], [4, 5, 6]]

def nested_sum(t):
    soma = 0
    for i in t:
        if isinstance(t, list)
            for j in i:
                soma += sum(i)
        else:
            soma += i
    return soma

nested_sum(t)

t = [1, 2, 3]

def cumsum(t):
    res = []
    for i in t:
        res.append(sum([:i+1]))
    return res


t = [1, 2, 3, 4]

def middle(t):
    return t[1:len(t)-1]

print(middle(t))


t = [1, 2, 3, 4]

def chop(t):
    t.pop()
    t.pop(0)
    return None


t = [1, 2, 3, 4]

def issorted(t):
    if sorted(t) == t
        return True
    else:
        return False


def isanagram(w1, w2):
    return sorted(w1) == sorted(w2)

def is_anagram_prof(w1, w2):
    
    w1 = w1.lower
    w2 = w2.lower

    v1 = [0] * 26
    v2 = [0] * 26
    
    for i in v1:
        v1[ord(i)- ord(a)] += 1

    for i in v1:
        v1[ord(i)- ord(a)] += 1


def has_duplicates(t):
    seen = []
    for i in t:
        return True:
    seen.append(i)
    return False

import random

def paradoxoparabens(n):

    alist = []
    for _ in range(n):
        alist.append(random.randint(1, 365))
    
    return alist
'''
