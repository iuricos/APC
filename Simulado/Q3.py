c1, n1 = input().split()
c2, n2 = input().split()
c3, n3 = input().split()

v1 = v2 = v3 = 0


while True:
    v = input()

    if v == n1:
        v1 += 1

    elif v == n2:
        v2 += 1

    elif v == n3:
        v3 += 1
    else:
        None

    if v == '':
        break

if v1>v2 and v1>v3:
    print(f'{c1} venceu com {v1} votos!')
elif v2>v1 and v2>v3:
    print(f'{c2} venceu com {v2} votos!')
elif v3>v1 and v3>v2:
    print(f'{c3} venceu com {v3} votos!')
else:
    if v1 == v2 == v3:
        print('Empate, entre 3 chapas...')
    elif v1 == v2 or v2 == v3 or v3 == v1:
        print('Empate, entre 2 chapas...')
