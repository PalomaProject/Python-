"""desafio 13 : faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com
15% de aumento""" 

salario = float(input('qual é o salario do funcionario? R$'))
aumento = salario + (salario*15/100)

print('um funcionario que ganhava R${}, com aumento de 15% passa a ganhar R${:.2f}' .format(salario,aumento))
