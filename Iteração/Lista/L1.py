soma = 0
parar = False
i = 0

while not parar:
    nome, sal = input().split(",")

    if nome == "Fim":
        parar = True
        
    else:
        soma += float(sal)
        i += 1

if i == 0 :
    print("0.00")
else:
    print(f'{soma/i:.2f}')
    