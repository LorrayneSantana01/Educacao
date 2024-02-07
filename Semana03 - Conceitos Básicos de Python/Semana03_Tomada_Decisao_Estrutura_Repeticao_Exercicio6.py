#Crie um programa que solicite ao usuário um login e uma senha. O programa deve permitir o acesso
#apenas se ousuário for "admin" e a senha for "admin123", caso contrário imprima uma mensagem de erro.

def login_input():
    return input('Digite aqui seu login: ')

def senha_input():
    return input('Digite aqui sua senha: ')

while True:
    login = login_input()
    senha = senha_input()
    
    if login == 'admin' and senha == 'admin123':
        print('Sucesso. Login será executado')
        break
    print('Login ou senha inválido.')