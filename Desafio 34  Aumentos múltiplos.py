''' Desafio: escreva um programa que pergunte o salario de um funcionario e calcule
o valor do seu aumento. para salarios superiores a R$ 1.250,00 calcule um aumento de 10%.
Para inferiores ou iguais aumento é de 15%. '''

salario = float(input('qual é o salario do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15/100)
else:
    novo = salario + (salario * 10/100)
print('quem ganhava R${:.2f} agora passa a ganhar R${:.2f}' .format(salario,novo))
        
