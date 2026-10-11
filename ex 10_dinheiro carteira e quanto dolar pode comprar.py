### Exercício 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

carteira = float(input('Seu dinheiro na conta: '))
dolar = 4.99 #essa variável indica o valor do dolar, caso altere dependendo da cotação

print(f'Com R${carteira} você pode comprar {carteira/dolar:.2f}US$')

####### para saber o inverso, com determinado valor em dolar, quanto consigo comprar de reais (se eu tenho dólares, quantos reais isso vale?)

# carteira = float(input('Seu dinheiro em dólar na conta: '))

#print(f'Com US$ {carteira}, você pode comprar {carteira*4.99:.2f}R$') # DOLAR PARA REAL = MULTIPLICA PELA COTAÇÃO