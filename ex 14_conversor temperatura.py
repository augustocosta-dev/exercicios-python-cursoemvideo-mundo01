# Exercício 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

tc =  float(input('Qual a temperatura em graus celsius?: '))
tf = tc * 1.8 + 32 # a formúla para converter celsius em fahrenheit é: F = C * 1.8 + 32
print(f'{tc} Cº em Fahrenheit é: {tf} Fº')