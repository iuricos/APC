import unicodedata

x = input()
normal = unicodedata.normalize('NFKD', x)

print(normal)