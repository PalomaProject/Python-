"""Desafio 037 - escreva um programa que leia um numero inteiro qualquer e peça para o usuário
escolher qual será a base de conversão:
1 para binario,
2- para octal,
3-para hexadecimal"""

num = int(input('digite um numero inteiro'))
print('''escolha uma das bases de conversão:
[1] converter para binario
[2] converter para octal
[3] converter para hexadecimal''')

opção = int(input('sua opção: '))

if opção == 1:
    print('{} convertido para binario é igual a {}' .format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para octal é igual a {}' .format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é igual a {}' .format(num, hex(num)[2:]))
else:
    print('opção invalida, tente novamente')
