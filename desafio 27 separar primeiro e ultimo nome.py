"""faça um programa que leia o nome completo de uma pessoa. mostrando em seguinda o primeiro e o ultimo
nome separadamente."""

nome = str(input('digite seu nome')).strip()
nomes = nome.split()
print(f'o primeiro nome é {nomes[0]} e o ultimo é {nomes[-1]}')
