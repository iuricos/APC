
def checa_poneglifo(n, poneglifo):
    if n%2==0:
        if poneglifo == poneglifo[::-1]:
            return True
        else:
            return False
    else:
        if poneglifo[:(n//2)] == poneglifo[:(n//2):-1] and poneglifo[(n//2)].count('X') == 1:
            return True
        else:
            return False

n = int(input())
poneglifo = []

for i in range(n): #Normaliza o poneglifo
    aux = input().split()
    for i in range(len(aux)):
        if aux[i] == 'X':
            aux[i] = 'X'
        elif aux[i] != 'O':
            aux[i] = 'O'
    poneglifo.append(aux)

#print(n)
#print(checa_poneglifo(n, poneglifo))
#print(poneglifo)
if checa_poneglifo(n, poneglifo):
    print('O one piece eh real!')
else:
    print('Talvez o tesouro seja os amigos que fizemos no caminho')