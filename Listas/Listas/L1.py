aux = input().split()
n = int(input())
multiplos = []

for i in range(len(aux)):
    aux[i] = int(aux[i])
 
for num in aux:
    if num%n == 0:
        multiplos.append(num)
       
print(*multiplos)