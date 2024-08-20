def impar(x):
    if x % 2 == 0:
        return False
    return True

def ultimo_digito(x):
    return x % 10

def correcoes(x):
    if impar(x):
        print('O número é ímpar...')
        print(f'O último dígito do número é {ultimo_digito(x)}.')
        print(f'O número corrigido é {x+1}.')
    else:
        print('O número é par...')
        print(f'O último dígito do número é {ultimo_digito(x)}.')
    
    
