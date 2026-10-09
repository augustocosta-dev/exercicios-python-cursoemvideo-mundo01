# Desafio 004
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e
# todas as informações possíveis sobre ele.

algo = input("Digite algo: ")
print(f'o tipo primitivo desse valor é {type(algo)}')
print(f'Só tem espaços? {algo.isspace()}')
print(f'é númerico? {algo.isnumeric()}')
print(f'é alfabetico? {algo.isalpha()}')
print(f'é alfanumerico? {algo.isalnum()}')
print(f'é maiúscula? {algo.isupper()}')
