#Desenvolver um programa que solicite a idade do usuário e identifique se ele é uma criança,
#um adolescente, adulto ou idoso.

def idade_usuario_input():
    return int(input('Digite aqui sua idade: '))

while True:
    idade_usuario = idade_usuario_input()
    if idade_usuario >= 0 and idade_usuario <= 11:
        print('Você é uma criança.')
        break
    elif idade_usuario >= 11 and idade_usuario <= 18:
        print('Você é um(a) adolescente.')
        break
    elif idade_usuario >= 19 and idade_usuario <= 59:
        print('Você é um adulto.')
        break
    elif idade_usuario >= 60 and idade_usuario <= 123:
        print('Você é um(a) idoso(a).')
        break
    print('Idade inválida!')