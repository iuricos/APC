msal = 0
parar = False
i = 0

while True:
    nome, sal = input().split(",")

    if nome == "Fim":
        break
    else:
        if float(sal) > float(msal):
            msal = sal
        i += 1

if i == 0:
    print("Não tem")
else:
    print(msal)