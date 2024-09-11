txt = input()
dicio = {}

def invert_dict(d):#revertendo usando setdefault()
    inv = {}
    for char in d:
        inv.setdefault(d[char], []).append(char)          
    return inv

for i in txt:
    if i in dicio:
        dicio[i] += 1
    else:
        dicio[i] = 1


print(dicio)
print(invert_dict(dicio))
        