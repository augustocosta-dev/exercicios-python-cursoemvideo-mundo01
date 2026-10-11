#Exercício 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float (input('Digite seu salário: '))
aumento = (salario * 15) / 100
salario_novo = salario + aumento

print(f'O seu salário de R$ {salario:.2f}, com aumento de 15% fica: R$ {salario_novo:.2f}')