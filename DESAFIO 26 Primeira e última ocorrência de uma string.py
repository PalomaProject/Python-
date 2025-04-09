"""Desafio 26: faça um programa que leia uma frase no teclado e mostre:
    -Quantas vezes aparece a letra 'A'
    -Em que posição ela aparece pela primeira vez
    -Em que posição ela aparece pela ultima vez"""


frase = str(input('digite uma frase')).upper()
a = frase.count('A')
print('A letra A aparece {} vezes' .format(a))

f = frase.find('A')
print('a primeira letra A apareceu na posição {}' .format(f + 1))

r = frase.rfind('A')
print('a ultima letra A apareceu na posição {}' .format(r + 1))


"""frase = str(input('escreva uma frase')).upper().strip
print('a letra A aparece {} vezes na frase' .format(frase.count('A'))) 
print('a primeira letra A apareceu na posição {}' .format(frase.find('A')+1))
print('a ultima letra A apareceu na posição {} ' .format(frase.rfind('A')+1))"""


#O MODO .upper() É PARA COLOCAR TODAS AS LETRAS DA FRASE EM MAIUSCULO, ISSO VAI AJUDAR NA HORA DE...
#IDENTIFICAR QUANTAS LETRAS "A" E NÃO VAI SEPARAR MAIUSCULAS DE MINUSCULAS. JÁ O .strip É PRA ELIMINAR
#ESPAÇOS DESNECESSARIOS NO INICIO E NO FIM DA FRASE, CASO O USUARIO COLOQUE SEM QUERER. JÁ O .count('A')
#É PRA CONTAR QUANTOS "A" EXISTEM NA FRASE, JÁ O .find('A') PRA ACHAR O PRIMEIRO "A" E O rfind('A')
#PRA ACHAR O ULTIMO 'A' NA FRASE, JÁ QUE ELE COMEÇA A CONTAR APARTIR DO FINAL DA FRASE. O +1 É PRA
#COMEÇAR A CONTAGEM APARTIR DO NUMERO 1, AO INVÉS DO ZERO.
            
