#Solicite ao usuário o número de horas de exercício físico por semana. Calcule o total de calorias
#queimadas em um mês, considerando uma média de 5 calorias por minuto de exercício.

quantidade_horas = float(input('Digite aqui a quantidade de horas de exercício físico você fez essa semana: '))

quantidade_minutos = quantidade_horas*60

quantidade_calorias_minuto = quantidade_minutos*5

quantidade_calorias_mes = quantidade_calorias_minuto*30

print(f'Você gastou {quantidade_calorias_mes:.10f} calorias essa semana!')