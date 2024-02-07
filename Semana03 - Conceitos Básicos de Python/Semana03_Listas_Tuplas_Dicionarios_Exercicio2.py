#Faça um programa que peça as quatro notas de 5 alunos, calcule e armazene numa lista a média
#de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

notas = []

for i in range(5):
    aluno = input(f"Digite o nome do {i + 1}º aluno: ")
    notas_aluno = []
    for j in range(4):
        nota = float(input(f"Digite a {j + 1}ª nota de {aluno}: "))
        notas_aluno.append(nota)
    
    media_aluno = sum(notas_aluno) / len(notas_aluno)
    
    notas.append(media_aluno)

numero_aprovados = 0
for media in notas:
    if media >= 7.0:
        numero_aprovados += 1

print(f"Número de alunos com média maior ou igual a 7.0: {numero_aprovados}")