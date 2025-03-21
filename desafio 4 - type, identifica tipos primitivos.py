"""Desafio 4: faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possiveis sobre ela"""


algo = (input('digite algo'))

print('o tipo primitivo é' ,type(algo))

print('Só tem espaço?')
print(algo.isspace())
print('é um numero?')
print(algo.isnumeric())
print('é alfabetico?')
print(algo.isalpha())
print('é alfanumerico?')
print(algo.isalnum())
print('está em maisculas?')
print(algo.isupper())
print('está em minusculas?')
print(algo.islower())
print('está capitalizada?')
print(algo.istitle())


#NÃO CONSEGUIR FAZER SEM OLHAR, PRECISO TREINAR MAIS.
