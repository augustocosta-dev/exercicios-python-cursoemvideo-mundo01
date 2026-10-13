'''
Exercício 015: Escreva um programa que pergunte a quantidade
de Km percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''
kmper = float(input('Quantos km você andou?: '))
alugueldia = int(input('Quantos dias você alugou?: '))
kmper_valor = kmper * 0.15
alugueldia_valor = alugueldia * 60.00
total = kmper_valor + alugueldia_valor
print(f'Se você percorrer {kmper} km, o valor a pagar irá ser de: R$ {kmper_valor:.2f}')
print(f'Se você alugar por {alugueldia} dias, o valor a pagar irá ser de: R$ {alugueldia_valor:.2f}')
print(f'o valor total ficou: R$ {kmper_valor+alugueldia_valor:.2f}')

## print(f'o valor total ficou: R$ {total}') #esse total funciona para deixar o código mais limpo, opcional.
