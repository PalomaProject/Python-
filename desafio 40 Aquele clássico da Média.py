'''Desafio 40 : crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem final,
de acordo com a  média atingifa:
média abaixo de 5.0: reprovado
média entre 5.0 a 6.9: recuperação
média 7.0 ou superior: aprovado.
'''

nota1 = float(input('digite a primeira nota'))
nota2 = float(input('digite a segunda nota'))

media = (nota1 + nota2) / 2

print('a sua media ficou {}' .format(media))

if media < 5:
    print('reprovado')
    
elif media < 6.9:
    print('recuperação')
    
else :
    print('aprovado')
