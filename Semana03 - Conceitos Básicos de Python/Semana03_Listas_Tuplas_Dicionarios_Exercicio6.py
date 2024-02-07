#Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário
#de trás para frente utilizando somente letras maiúsculas. 
#Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

nome_usuário = input('Digite aqui o seu nome: ')

def inverter_nome(nome):
     
  nome_invertido = ""
  for letra in nome:
    nome_invertido = letra + nome_invertido
  return nome_invertido.upper()

nome_invertido = inverter_nome(nome_usuário)
print(f'Seu nome de trás para frente em letras maiúsculas é: {nome_invertido}')