'''Desafio 41: A confederação nacional de natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
'''

nascimento = int(input('ano do seu nascimento?'))
ano = int(input('ano atual?'))

soma = ano - nascimento

print('a sua idade é {}' .format(soma))


if soma < 9:
    print('de acordo com a sua idade, sua categoria é MIRIM')
elif soma < 14:
    print('de acordo com a sua idade, sua categoria é INFANTIL')
elif soma <= 19:
    print('de acordo com a sua idade, sua categoria é JUNIOR')
elif soma < 20:
    print('de acordo com a sua idade, sua categoria é SENIOR')
else:
    print('de acordo com a sua idade, sua categoria é MASTER')

print('FIM')
