"""Desafio 45 GAME: crie um programa que faça o computador jogar pedra, papel e tesoura com vc."""

from random import randint

print('Suas opções:')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')

jogador = int(input('qual é a sua jogada?'))
computador = randint(-0,2)


if jogador == computador :
    print('empate')

elif jogador == 0 and computador == 1:
    print('computador venceu')
elif jogador == 1 and computador == 2:
    print('computador venceu')    
elif jogador == 2 and computador == 0:
    print('computador venceu')

elif jogador == 1 and computador == 0:
    print('jogador venceu')
elif jogador == 2 and computador == 1:
    print('jogador venceu')    
elif jogador == 0 and computador == 2:
    print('jogador venceu')

else:
    print('jogada invalida, tente novamente')

print('o jogador jogou {} e computador jogou {}' .format(jogador, computador))



