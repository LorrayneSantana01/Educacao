#Escreva um programa que calcule o salário líquido. Lembrando de declarar o salário bruto e o percentual
#de descontodo Imposto de Renda.
#● Renda até R$ 1903.98: isento de imposto de renda;
#● Renda entre R$ 1903.99 e R$ 2826.65: alíquota de 7,5%;
#● Renda entre R$ 2826.66 e R$ 3751.05: alíquota de 15%;
#● Renda entre R$ 3751.06 e R$ 4664.68: alíquota de 22,5%
#● Renda acima de R$ 4664.68: alíquota máxima de 27,5%.

salario_bruto = float(input('Digite aqui seu salário bruto: '))

if salario_bruto <= 1903.98:
    print(f'Seu salário líquido é {salario_bruto}!')
elif salario_bruto >= 1903.99 and salario_bruto <= 2826.65:
    print(f'Seu salário líquido é {salario_bruto - (salario_bruto*0.075)}!')
elif salario_bruto >= 2826.66 and salario_bruto <= 3751.05:
    print(f'Seu salário líquido é {salario_bruto - (salario_bruto*0.15)}!')
elif salario_bruto >= 3751.06 and salario_bruto <= 4664.68:
    print(f'Seu salário líquido é {salario_bruto - (salario_bruto*0.225)}!')
else: salario_bruto >= 4664.68
print(f'Seu salário líquido é {salario_bruto - (salario_bruto*0.275)}!')