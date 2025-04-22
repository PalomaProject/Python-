"""Desafio 44: elabore um programa que calcule o valor a ser pago por um produto, considerando o seu..
..preço normal e condição de pagamento:
- a vista dinheiro/cheque: 10% de desconto.
- a vista no cartão: 5% de desconto.
- em até 2x no cartão: preço normal.
- 3x ou mais no cartão:20% de juros"""

preço = float(input('qual é o valor da compra?R$'))
print("""FORMAS DE PAGAMENTOS:
[1] A vista dinheiro/cheque
[2] a vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")

opção = int(input('qual é a opção?'))

if opção == 1:
   print('o valor final da compra será R${:.2f}' .format(preço - (preço * 10/100)))
elif opção == 2:
   print('o valor final da compra será R${:.2f}' .format(preço - (preço * 5/100)))
elif opção == 3:
   print('o valor final da compra será R${:.2f}' .format(preço))
else:
   print('o valor final da compra será R${:.2f}' .format(preço + (preço * 20/100)))

print('FIM')

