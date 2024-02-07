#Faça um programa que lê três números inteiros e os mostra em ordem crescente.

numero1 = int(input('Digite aqui o primeiro número: '))
numero2 = int(input('Digite aqui o segundo número: '))
numero3 = int(input('Digite aqui o terceiro número: '))

def ordenar_crescente(numero1, numero2, numero3):

    if numero1 < numero2:
        numero1, numero2 = numero2, numero1

    if numero1 < numero3:
        numero1, numero3 = numero3, numero1

    if numero2 < numero3:
        numero2, numero3 = numero3, numero2

    return numero1, numero2, numero3

print(f"Os números em ordem crescente são: {numero1}, {numero2}, {numero3}")