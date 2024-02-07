#Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um 
#triângulo e classifique-o como equilátero, isósceles ou escaleno.
#equilátero: todos os lados com o mesmo valor;
#isósceles: dois lados com o mesmo valor;
#escaleno: todos os lados com medidas distintas.

comprimento1 = float(input('Digite aqui o primeiro comprimento: '))
comprimento2 = float(input('Digite aqui o segundo comprimento: '))
comprimento3 = float(input('Digite aqui o terceiro comprimento: '))

if comprimento1 == comprimento2 == comprimento3:
    print('O trinângulo é EQUILÁTERO!')
elif comprimento1 == comprimento2 or comprimento1 == comprimento3 or comprimento2 == comprimento3:
    print('O trinângulo é ISÓCELES!')
else: print('O trinângulo é ESCALENO!')

