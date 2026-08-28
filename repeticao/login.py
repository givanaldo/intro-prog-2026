login_padrao = "aluno"
senha_padrao = "ifrn123"
login = ""
senha = ""

while login != login_padrao or senha != senha_padrao:
    login = input("Login: ")
    senha = input("Senha: ")
    if login != login_padrao or senha != senha_padrao:
        print("Acesso inválido, tente novamente!")
    else:
        print("Acesso liberado!")

print("Restante do código")
