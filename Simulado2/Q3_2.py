s = input()
d = {}
d_inv = {}

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for letra in d:
    d_inv.setdefault(d[letra], []).append(letra)




#for letra in d:
#    if d[letra] in d_inv:
#        d_inv[d[letra]].append(letra)
#    else:
#        d_inv[d[letra]] = [letra]



print(d)
print(d_inv)