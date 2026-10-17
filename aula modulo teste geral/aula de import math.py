#@ 01 - importando a biblioteca inteira

import math
n = float(input('digite um número: '))
raiz = math.sqrt(n)
    # print(f'a raiz de {n} é {raiz:.2f}') #usando apenas variável sem a biblioteca
print(f'a raiz de {n} arrendondando para cima é {math.ceil(raiz)}') #usando a biblioteca CEIL para arredondar para cima
print(f'a raiz de {n} arredondando para baixo é {math.floor(raiz)}') #usando a biblioteca FLOOR para arredondar para baixo
print(f'a raiz quadrada de {n} é {math.sqrt(n):.2f} ')

#@ 02 - usando função específica da biblioteca

from math import sqrt
n = int(input('digite um numero: '))
raiz = sqrt(n)
print(f'a raiz de {n} é {raiz:.2f}')

#@ 03 - biblioteca RANDOM

import random
n = random.randint(1, 10)
print(n)

