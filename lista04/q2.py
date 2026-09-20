usuario = senha = ""
while usuario == senha:
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario == senha:
        print("Usuário igual à senha!")
print("Agora deu certo!")