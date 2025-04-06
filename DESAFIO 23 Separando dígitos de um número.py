''' DESAFIO 23: Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados. ex: digite um numero: 1834,
a unidade desse numero é 4, dezena 3, centena 8, milhar 1 '''

num = int(input('informe um numero'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print ('analisando o numero {}' .format(num))
print ('unidade{}' .format(u))
print ('dezena{}' .format(d))
print ('centena{}' .format(c))
print ('milhar{}' .format(m))


#mais um que eu não conseguir fazer só
