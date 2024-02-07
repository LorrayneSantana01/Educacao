'''
print('Aqui está um pouco das anotações das aulas de Pyhton')

print('# Essa é uma forma de comentários')

print('Outra forma de fazer comentários é colocando três aspas simples no começo e outras três aspas simples no final')
'''
#print('Olá, Mundo!')

#print('Agora vamos aprender variáveis')
'''
print('INT - Inteiro. Exemplos: 1, 5, 20000, 4000')
numero_idade = int(input('Digite aqui sua idade: '))
print(f'Sua idade é {numero_idade} anos.')


print('FLOAT - Decimais. Exemplos: 1.5, 5.2, 20000.3, 4000.4')
numero_altura = float(input('Digite aqui sua altura: '))
print(f'Sua altura é {numero_altura:.2f} m.') # ":.xf" define quantas casas decimais eu quero que printa


print('STRING - Textos. Exemplos: "Lorrayne", "WoMarkersCode","Python"')
nome_completo = input('Digite aqui seu nome completo: ')
print(f'Seu nome completo é {nome_completo}.')


print('BOOL - Analógico. Exemplos: True (1), False(0)')
pedido_casamento = bool(input('Você aceitar casar comigo? '))
print(f'Você disse {pedido_casamento}!')

print('Olá, sua amada tem {} anos, tem {} m, seu nome é {}, e {} casar com você!'.format(22, 1.51, 'Lorrayne Barbara Nunes Santana', True))
'''

# print('Agora vamos aprender operações matemáticas')
'''
print('Soma = +')
numero_soma_1 = float(input('Digite aqui seu primeiro número: '))
numero_soma_2 = float(input('Digite aqui seu segundo número: '))
soma = numero_soma_1+numero_soma_2
print(f'A soma dos resultados são: {soma}.')


print('Subtração = -')
numero_subtracao_1 = float(input('Digite aqui seu primeiro número: '))
numero_subtracao_2 = float(input('Digite aqui seu segundo número: '))
subtracao = numero_subtracao_1-numero_subtracao_2
print(f'A subtração dos resultados são: {subtracao}.')


print('Multiplicação = *')
numero_multiplicacao_1 = float(input('Digite aqui seu primeiro número: '))
numero_multiplicacao_2 = float(input('Digite aqui seu segundo número: '))
multiplicacao = numero_multiplicacao_1*numero_multiplicacao_2
print(f'A multiplicação dos resultados são: {multiplicacao}.')


print('Divisão = /')
numero_divisao_1 = float(input('Digite aqui seu primeiro número: '))
numero_divisao_2 = float(input('Digite aqui seu segundo número: '))
divisao = numero_divisao_1/numero_divisao_2
print(f'A divisão dos resultados são: {divisao}.')


print('Divisão Inteira = // - Sem casas decimais')
numero_divisao_inteira_1 = float(input('Digite aqui seu primeiro número: '))
numero_divisao_inteira_2 = float(input('Digite aqui seu segundo número: '))
divisao_inteira = numero_divisao_inteira_1//numero_divisao_inteira_2
print(divisao_inteira)


print('Resto = % - Resto da divisãi')
numero_resto = 10
numero_resto %= 3
print(numero_resto)


print('Incremento = += - Adicionar mais algumas coisas')
numero_incremento = 5
numero_incremento += 1
print(numero_incremento)


print('Decremento = -= - Retirar mais algumas coisas')
numero_decremento = 10
numero_decremento -= 5
print(numero_decremento)
'''

#print('Agora vamos aprender ordem de precedência - É o que determina a ordem em que os operadores são processados')
'''
calculo_1 = 2+2*10
print(calculo_1)

calculo_2 = (2+2)*10
print(calculo_2)

calculo_3 = (2+2)*((10+2)*2)
print(calculo_3)
'''

#print('Agora vamos aprender operadores relacionais')
'''
print('Temos: == - Igual')
print('Temos: > - Maior')
print('Temos: >= - Maior ou igual')
print('Temos: < - Menor')
print('Temos: <= - Menor ou igual')
print('Temos: != - Diferente de')
'''

#print('Agora vamos aprender IF (se) e ELSE (se não)')
'''
numero_if_else = int(input('Digite aqui um número: '))
if numero_if_else >= 0:
    print('O número é positivo.')
else:
    print('O número é negativo.')


#print('Agora vamos aprender WHILE (enquanto)')

numero_while = int(input('Digite aqui um número: '))
while numero_while <= 0:
    numero_while = int(input('Digite aqui um número: '))
print(f'O número digitado foi {numero_while}.')
'''

#print('Agora vamos aprender FOR (para cada)')
'''
lista_sabores_sorvete_for = ['Oreo','Frutas Vermelhas','Titti Frutti', 'Sorbet', 'Prestígio']
for sabores in lista_sabores_sorvete_for:
    print(sabores)

'''
#print('Agora vamos aprender listas')

# Meu dever de casa é fazer funcionar: Enquando o input for diferente de 'Fim',
# continuar digitando mais valores e se for igual 'Fim', fazer a lista de tudo

#sabor_de_sorvete():
#lista_sabores_sorvete = []
#sabor_sorvete = input('Digite aqui os sabores de sorvete favoritos: ')
#while sabor_sorvete != 'Fim':
#    sabor_sorvete = input('Digite aqui os sabores de sorvete favoritos: ')
#lista_sabores_sorvete.append(sabor_sorvete)
#lista_sabores_sorvete.append('Oreo')
#lista_sabores_sorvete.append('Frutas Vermelhas')
#lista_sabores_sorvete.append('Titti Frutti')
#print(lista_sabores_sorvete)


#print('Agora vamos aprender tuplas')
'''
lista_frutas = ('Maça','Banana','Morango','Kiwi','Uva')
print(lista_frutas)
'''

#print('Agora vamos aprender dicionários')
'''
conjunto_palavras = {'Chave':'Valor'}
conjunto_palavras['Carro'] = 'É um veículo'
conjunto_palavras['Maça'] = 'É uma fruta'
conjunto_palavras['Calopsita'] = 'É um animal'
print(conjunto_palavras)
'''

#print('Agora vamos aprender funções')
'''
def soma():
    sum = 10+2
    print(f'O resultado dessa operação é {sum}.')
    multiplicacao()
    subtracao()

def subtracao():
    sub = 10-2
    print(f'O resultado dessa operação é {sub}.')

def multiplicacao():
    mult = 10*2
    print(f'O resultado dessa operação é {mult}.')

soma()
''' 
#print('Agora vamos aprender parâmetros')
'''
def soma(num1,num2):
    sum = num1+num2
    print(f'O resultado dessa operação é {sum}.')

def subtracao(num1,num2):
    sub = num1-num2
    print(f'O resultado dessa operação é {sub}.')

def multiplicacao(num1,num2):
    mult = num1*num2
    print(f'O resultado dessa operação é {mult}.')

num1 = int(input('Digite aqui o primeiro número: '))
num2 = int(input('Digite aqui o segundo número: '))

soma(num1,num2)
subtracao(num1,num2)
multiplicacao(num1,num2)
'''

#print('Agora vamos aprender manipulação de arquivos - Abrir (open), Escrever (w), Ler (r), Binários (wb)')
'''
file = 'arquivo.txt'

print('Abertura de arquivos para escrita')
arquivo_para_escrever = open(file, "w")
arquivo_para_escrever.write('Eu sei nadar!')
arquivo_para_escrever.close()

print('Abertura de arquivos para leitura')
arquivo_para_ler = open(file, "r")
leitura = arquivo_para_ler.read()
print(leitura)
arquivo_para_ler.close()

print('Abertura de arquivos binários')
arquivo_binario = open(file, "wb")
'''
#print('Agora vamos aprender tratamentos de erros')
'''
def divisao(a,b):
    try:
        resultado = a/b
        print(resultado)
    except ZeroDivisionError:
        print('Erro: Impossível dividir um número por zero.')
    except TypeError as e:
        print(f'O tipo do dado informado está incorreto!\nDetalhes: {e}')

divisao(10,2)
divisao(10,0)
divisao(10,'Uma frase qualquer')
'''