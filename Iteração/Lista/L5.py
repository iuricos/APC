PA, PB, T1, T2 = map(float, input().split())
PA, PB = int(PA), int(PB)
anos = 0

while PA < PB:

    if T1 <= T2:
        print("A nunca alcancara B.")
        break

    PA = int(PA + PA * (T1/100))
    PB = int(PB + PB * (T2/100))
    anos += 1

    if anos > 1000:
        print("Mais de um milenio.")
        break

    if PA >= PB:
        print(f'Vai alcancar em {anos} ano(s).')
        break