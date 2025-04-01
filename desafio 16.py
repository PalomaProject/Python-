"""" 16: crie um programa que leia um numero real qualquer e mostre na tela sua porção inteira """

import math 

numero = float(input('digite um valor'))
valor = math.trunc(numero)

print('o numero digitado foi {} e sua porção inteira é {}' .format(numero,valor))
