#DESAFIO 25: CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM "SILVA" NO NOME.

nome = str(input('qual o seu nome?')).strip()
print ('seu nome tem silva? {}' .format ('silva' in nome.lower()))
