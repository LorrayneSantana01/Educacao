#Faça um programa que pergunte em que turno você estuda. Peça para digitar 
#M-matutino ou V-Vespertino ou N-Noturno.
#Imprima a mensagem "BomDia!", "BoaTarde!" ou "BoaNoite!" ou "ValorInválido!", conforme o caso.

turno_usuario = input('Considere:\nM para Matutino\nV para Vespertino\nN para Noturno.\nDigite aqui o turno em que você estuda: ')

if turno_usuario == "M":
    print('Você estuda no turno Matutino.')
elif turno_usuario == "V":
    print('Você estuda no turno Vespertino.')
else: turno_usuario == "N"
print('Você estuda no turno Noturno.')