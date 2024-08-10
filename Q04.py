login = input("Login: ")
senha = int(input("Senha: "))

if login == "admin" and senha == 123:
    print('Olá admin, seja bem-vindo!')

elif login == "admin" and senha != 123:
    print('Login ou senha incorretos, tente novamente.')

elif login != "admin" and senha == 123:
    print('Login ou senha incorretos, tente novamente.')
    
else:
    print('Login ou senha incorretos, tente novamente.')