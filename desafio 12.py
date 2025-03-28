"""Desafio 12 : faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5%
de desconto. """

preço = float(input('qual é o preço do produto? R$'))
desconto = preço * 5/100
desconto2 = preço - desconto

print('o produto que custava R${}, com a promoção de 5% passa a custar R${:.2f}' .format(preço,desconto2))


    
