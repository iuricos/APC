n = int(input())

divisores = []

for i in range(n):
    if i%3 == 0 and i%7 == 0:
       divisores.append(str(i))
    concatenada = " ".join(divisores)

print(concatenada) 