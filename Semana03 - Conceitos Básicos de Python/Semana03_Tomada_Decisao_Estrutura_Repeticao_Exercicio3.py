#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor 
#seja inválido e continue pedindo até que o usuário informe um valor válido.

nota_usuario = float(input('Digite aqui um número: '))

if nota_usuario >= 0 and nota_usuario <= 10:
    print('Sucesso. Você inseriu um número válido')
else: nota_usuario < 0 and nota_usuario > 10
print('Número inválido. Tente novamente. Digite aqui um número: ')