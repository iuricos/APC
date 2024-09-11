aux = input().split()
memo = {'d':0, 't':0, 'v':0}

for palavra in aux:
    for letra in palavra:
        if letra == 'd':
            memo['d'] += 1
        if letra == 'v':
            memo['v'] += 1
        if letra == 't':
            memo['t'] += 1

for c in memo:
    if memo[c] != 0:
        print(c, memo[c])
        
