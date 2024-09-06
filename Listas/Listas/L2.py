def soma_adinilson(l):
    if len(l) == 1:
        return l[0]
    else:
        l[1] = l[0] * 2 + l[1] * (1/2)
        l = l[1:]
        return soma_adinilson(l)
        
aux = list(map(int, input().split()))
n = soma_adinilson(aux)
print(f'{n:.2f}')