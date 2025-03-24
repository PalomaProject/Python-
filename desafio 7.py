"""Desafio 7 : Desenvolva um program que leia duas notas de um aluno e calcule a sua média"""


nota1 = float(input('qual foi a primeira nota?'))
nota2 = float(input('qual foi a segunda nota?'))

soma = nota1 + nota2
media = soma / 2

print('a media entre {} e {} é {}' .format(nota1,nota2,media))
