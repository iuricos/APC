a = input()

def simples(a):
    if a == "repete":
        print('Olá! Vamos repetir!')
        simples(input())

simples(a)