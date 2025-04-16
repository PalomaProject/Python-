"""Desafio 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a
sua idade:
-se ele ainda vai se alistar ao serviço militar.
-se é a hora de se alistar.
-se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. """


nascimento = int(input('em que ano vc nasceu?'))
ano = int(input('qual é o ano atual?'))

diminuir = ano - nascimento
sobra = 18 - diminuir

if diminuir < 18:
    print ('vc ainda não tem idade pra se alistar, falta {} anos' .format(sobra))
elif diminuir == 18:
    print('já está na hora de se alistar')
elif diminuir > 18:
    print('já passou {} anos do seu alistamento' .format(sobra))

print('FIM')
