### Exercício 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
### Ex: Digite um numero: 6.127 | O numero 6.127 tem a parte inteira 6 - (6).127

from math import trunc
n = float (input('digite um numero inteiro: '))
n2 = trunc (n)
print (f'o numero {n} tem a parte inteira {n2}')

