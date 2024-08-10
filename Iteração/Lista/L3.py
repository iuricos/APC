msal = 1000000000.00
mnome = ''
i = 0

while True:
    nome, sal = input().split(",")
    
    if nome == "Fim":
        break
    else:
        if float(sal) < float(msal):
            mnome = nome
            msal = sal
        i += 1

if i == 0:
    print("Não tem")
else:
    print(mnome)