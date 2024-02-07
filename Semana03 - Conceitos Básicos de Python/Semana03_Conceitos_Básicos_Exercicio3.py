#Faça um programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.

quantidade_quilometros = float(input('Digite aqui o quantidade de quilômetros: '))

metros = quantidade_quilometros*1000
centimetros = quantidade_quilometros*100000
milimetros = quantidade_quilometros*1000000

print(f'A quantidade em metros é {metros}!')
print(f'A quantidade em centímetros é {centimetros}!')
print(f'A quantidade em milímetros é {milimetros}!')
