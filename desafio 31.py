'''Desafio 31: desenvolva um programa que pergunte a distância de uma viagem em km. calcule o preço da passagem, cobrando R$0,50
por km para viagens de até 200km e R$ 0,45 para viagens mais longas.'''


distancia = float(input('qual é a distância da sua viagem'))


if distancia <= 200:
    soma = distancia * 0.50
    print('o valor a ser pago por essa distancia será R${}' .format(soma))
else:    
    soma2 = distancia * 0.45
    print('o valor a ser pago por essa distancia será R${}' .format(soma2))
