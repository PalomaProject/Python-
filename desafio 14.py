"""Desafio 14: Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF """

temperatura = float(input('qual é a temperatura em ºC?'))
convertido = ((9*temperatura)/5) + 32

print ('a temperatura de {}ºC corresponde a {}ºF' .format(temperatura,convertido))
