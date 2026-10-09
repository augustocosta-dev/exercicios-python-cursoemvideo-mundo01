# Exercício 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

## Modo que usei:

# n_m = int (input('digite sua metragem: '))
# n_cm = n_m * 100
# n_mm = n_m * 1000

# print(f'O seu número em centímetros é: {n_cm} cm')
# print(f'O seu número em milímetros é: {n_mm} mm')


## Modo ajustado:
    n_m = float (input('digite sua metragem: '))
    n_cm = n_m * 100
    n_mm = n_m * 1000

    print(f'O seu número em centímetros é: {n_cm:.2f} cm')
    print(f'O seu número em milímetros é: {n_mm:.2f} mm')