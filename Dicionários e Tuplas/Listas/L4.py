n = int(input())
infos = {}

for i in range(n):
    nome, email, n1, n2, n3, n4 = input().split()
    media = (float(n1)+float(n2)+float(n3)+float(n4))/4
    infos[nome] = {0:email, 1: media}

indigente = input()

if indigente in infos:
    print(f'Destinatário: {infos[indigente][0]}')
    if int(infos[indigente][1]) >= 5:
        print(f'O aluno {indigente} foi aprovado com média {infos[indigente][1]:.2f}.')
    else:
        print(f'O aluno {indigente} foi reprovado com média {infos[indigente][1]:.2f}.')
else:
    print(f'O aluno {indigente} não está na turma.')