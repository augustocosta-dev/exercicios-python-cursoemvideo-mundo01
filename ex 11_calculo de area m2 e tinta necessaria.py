'''
Exercício 011: Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro
de tinta pinta uma área de 2 metros quadrados.
'''

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print(f'A área da parede é {area}')
print(f'E a quantidade de tinta necessária será de: {(area)/2:.2f} litros')


'''
MELHORIA OPCIONAL: guardar o valor do calculo de tinta dentro de uma variável, para deixar mais legivel. 

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2

print(f'A área da parede é {area} m²')
print(f'A quantidade de tinta necessária será de: {tinta:.2f} litros')


'''