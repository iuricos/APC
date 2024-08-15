n = int(input())
chamada = []

for _ in range(n):
    chamada.append(input())

chamada.sort(reverse=True)

for i in chamada:
    print(i)
