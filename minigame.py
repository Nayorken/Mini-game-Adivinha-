from random import randint
print('Bem vindo!')
sortear = randint(1, 1000)
palpite = 0
while palpite != sortear:
    palpite = int(input('Palpite: '))
    if palpite == sortear:
        print('Você ganhou!')
    else:
        if palpite > sortear:
            print('Mais Baixo')
        else: 
            print('Mais Alto')
print('Fim do jogo!')
