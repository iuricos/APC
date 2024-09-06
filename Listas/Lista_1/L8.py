def fibonacci(n):
    if n == 0:
        vetor.append(n)
        return 0
    if n == 1:
        vetor.append(n)
        return 1
    if n > 1:
        vetor.append(n)
        return fibonacci(n-1) + fibonacci(n-2) 

vetor = []

n = int(input())

print(f'Termo: {fibonacci(n)}')
print("Quantidades:")
if n != 1:
    for i in sorted(set(vetor)):
        print(f'fibonacci({i}) - {vetor.count(i)}')
else:
    print(f'fibonacci(0) - 0')
    for i in sorted(set(vetor)):
        print(f'fibonacci({i}) - {vetor.count(i)}')

