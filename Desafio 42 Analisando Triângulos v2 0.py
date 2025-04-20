'''Desafio 42: refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
equilátero : todos os lados iguais
esósceles: dois lados iguais
escaleno: todos os lados diferentes '''


print('analisador de triângulo')

r1 = float(input('primeiro segmento'))
r2 = float(input('segundo segmento'))
r3 = float(input('terceiro segmento'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos acima podem formar um triângulo'  ,end=' ')
    if r1 == r2 == r3 :
        print('equilátero')
    elif r1 != r2!= r3:
        print('escaleno')
    else:
        print('isoseles')

else:
    print('os segmentos acima não podem formar triângulo')
    


    

