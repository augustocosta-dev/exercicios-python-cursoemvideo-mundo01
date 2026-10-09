### Exercício 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número. Ele irá lhe informar o dobro, o triplo e sua raiz quadrada: '))
n_dobro = n * 2
n_triplo = n * 3
n_raiz = n**(1/2)

print(f'O seu número é {n}. O seu dobro é {n_dobro}, seu triplo é {n_triplo} e sua raiz quadrada é {n_raiz:.5f}')
#print('O número foram alterados para flutuantes, usando FLOAT em N.')