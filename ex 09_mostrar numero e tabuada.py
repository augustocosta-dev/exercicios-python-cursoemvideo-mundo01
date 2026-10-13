## Exercício 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um número e saiba a sua tabuada de multiplicação: '))

# tab_1 define a variável n multiplicada pela sequencia a ser definida
tab_1 = n*1
tab_2 = n*2
tab_3 = n*3
tab_4 = n*4
tab_5 = n*5
tab_6 = n*6
tab_7 = n*7
tab_8 = n*8
tab_9 = n*9
tab_10 = n*10

print(f'A tabuada do número {n} está abaixo:\n')

#print aqui está correto, porém, como no comentário abaixo, não seria necessário criar inúmeras variáveis
print('--------')
print(f'{n} x 1 = {tab_1}')
print(f'{n} x 2 = {tab_2}')
print(f'{n} x 3 = {tab_3}')
print(f'{n} x 4 = {tab_4}')
print(f'{n} x 5 = {tab_5}')
print(f'{n} x 6 = {tab_6}')
print(f'{n} x 7 = {tab_7}')
print(f'{n} x 8 = {tab_8}')
print(f'{n} x 9 = {tab_9}')
print(f'{n} x 10 = {tab_10}')
print('--------')

"""
Variáveis desnecessárias

Você não precisa guardar cada resultado numa variável. Dá para calcular direto dentro do print, porque o f-string aceita expressões:

python
n = int(input('Digite um número: '))

print(f'A tabuada do número {n} está abaixo:\n')
print(f'{n} x 1 = {n*1}')
print(f'{n} x 2 = {n*2}')
print(f'{n} x 3 = {n*3}')
print(f'{n} x 4 = {n*4}')
print(f'{n} x 5 = {n*5}')
print(f'{n} x 6 = {n*6}')
print(f'{n} x 7 = {n*7}')
print(f'{n} x 8 = {n*8}')
print(f'{n} x 9 = {n*9}')
print(f'{n} x 10 = {n*10}')



"""
