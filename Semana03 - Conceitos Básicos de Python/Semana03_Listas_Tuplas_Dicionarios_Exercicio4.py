#Crie um dicionário representando contatos (nome, telefone). Permita ao usuário procurar
#por um contato pelo nome.

telefone_contatos= {
    'Ana': '3191234-5678',
    'João': '2191234-5678',
    'Maria': '7191234-5678',
    'Zé': '2291234-5678',
    'Tereza': '3791234-5678',
}

procurar_contato = input('Digite aqui o nome do contato: ')

if telefone_contatos.get(procurar_contato) is None:
    print(f"Essa pessoa não está na lista de contatos.")
else:
    print(f'O telefone que você procura é: {telefone_contatos.get(procurar_contato)}.')