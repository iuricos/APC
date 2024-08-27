qnt = tot = int(input())
salmedio = 0

nomemaior = str
salmaior = 0

nomemenor = str
salmenor = 10000000000000000000


while qnt != 0:
    n, v = input().split(',')
    v = float(v)
    
    if v > salmaior:
        nomemaior = n
        salmaior = v

    if v < salmenor:
        nomemenor = n
        salmenor = v

    salmedio += v

    qnt -= 1

print(f'{salmedio/tot:.2f}')
print(nomemaior, salmaior)
print(nomemenor, salmenor)