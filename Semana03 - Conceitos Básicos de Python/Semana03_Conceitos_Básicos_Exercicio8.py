#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input('Digite aqui quanto você ganha por hora: '))
quantidade_horas = float(input('Digite aqui a quantidade de horas que você trabalhou no mês: '))

salario = valor_hora * quantidade_horas

print(f'Esse mês o seu salário é de {salario}!')