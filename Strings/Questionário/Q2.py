aux = input()
R2 = 0
R1 = True
R3 = False

if aux.isupper() or aux.islower():
    R1 = False

for i in aux:
    if not i.isalnum():
        R2 += 1

if 6 < len(aux) < 32:
    R3 = True

if R1 and (R2==0) and R3:
    print("Senha valida.")
else:
    print("Senha invalida.")