aux = input()
nova = ''
i = 0

for c in aux:
    if (i % 2) != 0:
        nova += c
    i += 1

print(nova.replace(" ", ""))
