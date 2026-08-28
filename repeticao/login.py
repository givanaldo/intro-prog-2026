login_padrao = "aluno"
senha_padrao = "ifrn123"
login = ""
senha = ""

while True:
    login = input("Login: ")
    senha = input("Senha: ")
    if login != login_padrao or senha != senha_padrao:
        print("Acesso inválido, tente novamente!")
    else:
        print("Acesso liberado!")
        break

print("Restante do código")
