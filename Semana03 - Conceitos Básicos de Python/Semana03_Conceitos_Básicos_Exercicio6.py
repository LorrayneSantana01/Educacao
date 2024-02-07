#Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de avião,
#carro e ônibus. Levando em consideração:
#● Avião = 600 km/h
#● Carro = 100 km/h
#● Ônibus = 80 km/h

quantidade_quilometros = float(input('Digite aqui a distância da sua viagem: '))

tempo_aviao = quantidade_quilometros/600
tempo_carro = quantidade_quilometros/100
tempo_onibus = quantidade_quilometros/80

print(f'O percurso de avião leva {tempo_aviao:.2f} horas para ser realizado!')
print(f'O percurso de carro leva {tempo_carro:.2f} horas para ser realizado!')
print(f'O percurso de ônibus leva {tempo_onibus:.2f} horas para ser realizado!')