N, M, K = map(int, input().split())
equipes = list(map(int, input().split()))
quantidade_agenciados = list(map(int, input().split()))

agenciados = []
for _ in range(M):
    agenciados.append(list(map(int, input().split())))

manipuladores = []

for i in range(M):
    equipes_agenciadas = set()
    for jogador in agenciados[i]:
        equipe = equipes[jogador - 1]
        equipes_agenciadas.add(equipe)
    
    if len(equipes_agenciadas) == K:
        manipuladores.append(i + 1)

if manipuladores:
    print(" ".join(map(str, sorted(manipuladores))))
else:
    print("-1")
