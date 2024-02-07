#Solicite ao usuário o peso em kg e a altura em metros. Calcule e imprima o Índice de Massa Corporal(IMC)
#usando a fórmula: IMC = peso / (altura x altura).

quilos_usuario = float(input('Digite aqui sua massa corporal: '))
altura_usuario = float(input('Digite aqui sua altura em m: '))

imc_usuario = quilos_usuario / (altura_usuario * altura_usuario)

print(f'Seu IMC é de {imc_usuario:.2f}!')