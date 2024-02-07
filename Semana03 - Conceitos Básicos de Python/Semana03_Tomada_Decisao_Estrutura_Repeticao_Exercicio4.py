#Implemente um programa que classifique um aluno com base em sua pontuação em um exame.
#O programa deverá solicitar uma nota de 0 a 10. Se a pontuação for maior ou igual a 7, o aluno é aprovado;
#caso contrário, é reprovado.

pontuacao_aluno = float(input('Digite aqui a pontuação do aluno: '))

if pontuacao_aluno < 0 or pontuacao_aluno > 10:
    float(input('Nota inserida inválida. Tente novamente! Digite aqui a pontuação do aluno: '))
elif pontuacao_aluno >= 0 or pontuacao_aluno < 7:
    print('Aluno foi REPROVADO!')
else: pontuacao_aluno >= 7 or pontuacao_aluno <= 10
print('Aluno foi APROVADO!')
