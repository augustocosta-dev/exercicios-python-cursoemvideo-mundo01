### Exercício 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
valor = float(input('Valor do produto: '))
desconto = (valor * 5)/ 100
valor_desconto = valor - desconto
print(f'o valor do produto com 5% de desconto é {valor_desconto:.2f} R$')

### codigo de como poderia ser o racicionio original, gerado pelo claude e orientado

"""
valor = float(input('Valor do produto: R$ '))
desconto = (valor * 5) / 100
novo_preco = valor - desconto
print(f'O produto custava R$ {valor:.2f}, e com 5% de desconto vai custar R$ {novo_preco:.2f}')

"""""