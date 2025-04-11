#Desafio 30: crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar.

n = int(input('digite um numero'))

soma = n / 2
s = soma % 1
if s :
    print('esse numero é IMPAR')

else:
    print('esse numero é PAR')

     
