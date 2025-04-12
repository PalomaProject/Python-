#Desafio 33 : faça um programa que leia 3 numeros e diga qual é o menor e o maior.

n1 = int(input('digite um numero'))
n2 = int(input('outro numero'))
n3 = int(input('mais um numero'))

if n1 > n2 and n1 > n3:
     print(' {} é o maior numero' .format(n1))
elif n2 > n3 and n2 > n1:
     print(' {} é o maior numero' .format(n2))
elif n3 > n1 and n3 > n2:
     print(' {} é o maior numero' .format(n3))
    
if n1 < n2 and n1 < n3:
     print(' {} é o menor numero' .format(n1))     
if n2 < n1 and n2 < n3:
         print(' {} é o menor numero' .format(n2))
elif n3 < n2 and n3 < n1:
         print(' {} é o menor numero' .format(n3))

