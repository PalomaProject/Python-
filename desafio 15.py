"""Desafio 15: escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. calcule o preço a pagar, sabendo que o carro
custa R$60 por dia e R$0,15 por km rodado"""

dia = int(input('quantos dias foram alugados?'))
km = float(input('quantos km rodados'))

dias = dia * 60
ki = km * 0.15
soma = ki + dias

print('o total a pagar é R${}' .format(soma))

