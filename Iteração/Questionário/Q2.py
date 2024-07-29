qnt = tot = int(input())
maior = -100000000.00
menor = 1000000000.00
nome_maior = str
nome_menor = str
media = 0


if qnt == 0:
    print(f"Não tem média\nNão tem\nNão tem")
else:
    while qnt != 0:
        nome, sal = input().split(",")
        sal = float(sal)
        media += sal
        if sal > maior:
            maior = sal
            nome_maior = nome
        if sal < menor:
            menor = sal
            nome_menor = nome
        
        qnt -= 1
    media = media/tot
    print(f'{media:.2f}\n{nome_maior} {maior:.2f}\n{nome_menor} {menor:.2f}')


