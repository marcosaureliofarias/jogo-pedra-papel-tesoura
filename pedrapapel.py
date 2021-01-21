from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opcoes:
[ 0 ] Pedra
[ 1 ] papel
[ 2 ] tesoura''')
jogador = int(input('Qual e a sua jogada? '))
print('-=' *10)
print('Computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('-=' *10)
if computador == 0: 
    if jogador == 0:
        print('empate')
    elif jogador == 1:
        print('jogador vence')
    elif jogador == 2:
        print('computador vence')
    else:
        print('jogada inválida!')
elif computador == 1:
    if jogador == 0:
        print('computador vence')
    elif jogador == 1:
        print('empate')
    elif jogador == 2:
        print('jogador vence')
    
    else:
        print('jogada inválida!')
elif computador == 2:
    if jogador == 0:
        print('jogador vence')
    elif jogador == 1:
        print('computador vence')
    elif jogador == 2:
        print('empate')
    else:
        print('jogada inválida!')