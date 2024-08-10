aux = input()

if aux.find(" ") > 0:
   aux = aux[0:2] + aux[(aux.find(" ")+1):(aux.find(" ")+3)]

elif len(aux) == 3:
    aux = aux[0:2]

elif len(aux) >=3:
    aux = aux[0:3]

print(aux)