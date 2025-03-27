"""desafio 10 : crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
dolares ela pode comprar"""

dinheiro = float(input('quanto vc tem na carteira? R$'))
dolar = dinheiro / 4.92

print ('com R${} você consegue comprar US{:.2f}' .format(dinheiro,dolar))
