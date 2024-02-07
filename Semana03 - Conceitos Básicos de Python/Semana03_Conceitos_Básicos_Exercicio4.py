#Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida.
#Calcule e imprima o consumo médio em km/l.

quantidade_litros = float(input('Digite aqui a quantidade de litros de combustível consumidos: '))
distancia_percorrida = float(input('Digite aqui a quantidade a distância percorrida em quilômetros: '))

consumo_medio = distancia_percorrida/quantidade_litros

print(f'O consumo médio é de {consumo_medio}!')