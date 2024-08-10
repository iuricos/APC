namigos, ingresso = input().split(" ")
namigos = int(namigos)
ingresso = int(ingresso)
adinheiro = 0
tot = 0


for i in range(namigos):
    adinheiro = int(input())
    tot += adinheiro

media = tot/namigos

if (media >= ingresso):
    print(f'media: {int(media)} \n  o rock reinara mais uma vez')
else:
    print(f'media: {int(media)} \n  rockeiros trabalhando ja')