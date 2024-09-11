n = int(input())
nomenota = {}
nomesporra = []

for i in range(n):
    nome, nota = input().split(', ')
    nomenota[nome] = float(nota)
    
nota_pessoal = float(input())

for nome in nomenota:
  if nota_pessoal == nomenota[nome]:
        nomesporra.append(nome)


nomesporra = sorted(nomesporra)

if nomesporra:
    for nome in nomesporra:
        if not nomesporra.index(nome) == len(nomesporra)-1:
            print(nome, end='/')
        else:
            print(nome)
else:
    print('Você foi o único aluno com essa nota.')