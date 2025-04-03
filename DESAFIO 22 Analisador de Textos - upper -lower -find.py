'''DESAFIO 22: CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E MOSTRE: O NOME COM TODAS LETRAS EM MAIUSCULA, MINUSCULAS, QUANTAS LETRAS AO TODO,
QUANTAS LETRAS TEM O PRIMEIRO NOME.'''

nome = str(input('qual é o seu nome completo?')).strip()
print ('analisando seu nome...')
print ('seu nome em letras maiusculas é {}' .format(nome.upper()))
print ('seu nome com letras minusculas é {}' .format (nome.lower()))
print ('seu nome tem {} letras ao todo' .format(len(nome)- nome.count(' ')))
print ('seu primeiro nome tem um total de {} letras' .format(nome.find(' ')))
                             

'''O COMANDO .strip() É PARA REMOVER O ESPAÇO NO INICIO E NO FIM, O len VER QUAL É O TAMANHO (QUANTAS LETRAS TEM NA FRASE), JÁ O -nome.count(' '),
CONTA O TAMANHO DA FRASE (LETRAS) REMOVENDO OS ESPAÇOS NO MEIO.
O COMANDO .find SERVE PRA LOCALIZAR DETERMINADA FRASE.'''



