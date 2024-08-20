aux = input()
c = input()

if c in aux:
    for i in aux:
        aux = aux.replace(c, "*")
    print(aux)
else:
    print("tudo certo :)")