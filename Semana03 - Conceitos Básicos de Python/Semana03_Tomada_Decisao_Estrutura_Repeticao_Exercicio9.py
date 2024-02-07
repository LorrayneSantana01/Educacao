#O programa deve calcular e apresentar a quantidade de números pares e ímpares inseridos. O processo de
#leitura deve ser encerrado quando o usuário informar o valor zero. Certifique-se de incluir validações
#para garantir que apenas números positivos sejam considerados na contagem e cálculos.

lista = []

while True:
    numero_input = int(input('Digite aqui um número: '))
    if numero_input == 0:
        break
    if numero_input < 0:
        print('Número inválido, digite apenas positivos.')
        continue
    lista.append(numero_input)

cont_pares = 0
cont_impares = 0
for numero in lista:
    if numero % 2 == 0:
        cont_pares = cont_pares + 1
    else: 
        cont_impares = cont_impares + 1
        
print(f'Os números pares são: {cont_pares}.\nOs números ímpares são: {cont_impares}.')