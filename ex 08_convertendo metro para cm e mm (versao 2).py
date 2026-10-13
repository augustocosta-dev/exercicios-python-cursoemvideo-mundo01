# Exercício 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

## Modo que usei:

# n_m = int (input('digite sua metragem: '))
# n_cm = n_m * 100
# n_mm = n_m * 1000

# print(f'O seu número em centímetros é: {n_cm} cm')
# print(f'O seu número em milímetros é: {n_mm} mm')


## Modo ajustado para mostrar toda a escala:
n_m = float (input('digite sua metragem: '))

print(f'O seu número em Kilômetros é: {n_m / 1000:.3f} Km')
print(f'O seu número em hectômetro é: {n_m / 100:.2f} Hm')
print(f'O seu número em decâmetro é: {n_m / 10:.1f} Dam')
print(f'O seu número em metros é: {n_m:.1f} m')
print(f'O seu número em decímetros é: {n_m * 10:.1f} dm')
print(f'O seu número em centímetros é: {n_m * 100:.1f} cm')
print(f'O seu número em milímetros é: {n_m * 1000:.1f} mm')