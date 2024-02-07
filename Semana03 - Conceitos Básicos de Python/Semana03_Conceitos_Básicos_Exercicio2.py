#Peça ao usuário para informar o ano de nascimento. Em seguida, calcule e imprima a idade atual.

ano_nascimento = int(input('Digite aqui o ano em que você nasceu: '))
ano_atual = int(input('Digite aqui o ano em que estamos: '))

subtracao = ano_atual-ano_nascimento

print(f'Você tem {subtracao} anos!')