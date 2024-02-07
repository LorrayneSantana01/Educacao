#Faça um programa que peça dois números e imprima o maior deles.

numero1 = float(input('Digite aqui o primeiro número: '))
numero2 = float(input('Digite aqui o segundo número: '))

if numero1 > numero2:
    print(f'O maior número é: {numero1}.')
else:
    print(f'O maior número é: {numero2}.')