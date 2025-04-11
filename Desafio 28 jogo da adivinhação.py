'''Desafio 28: escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 a 5 e peça pro usuario tentar descobrir
qual foi o numero escolhido pelo computador. o computador deverá escrever na tela se o usuario venceu ou perdeu.'''

from random import randint

computador = randint(0, 5) #faz o computador pensar
print('vou pensar em um numero entre 0 a 5, tente adivinhar...')
jogador = int(input('em que numero eu pensei?')) #jogador tenta adivinhar

print('processando')

sleep(3)

if jogador == computador:
    print('parabéns')
else:
    print('ganhei, eu pensei no numero {} e não no numero {} ' .format(computador,jogador))
