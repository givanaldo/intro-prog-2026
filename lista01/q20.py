nome = input("Primeiro nome: ")
sobrenome = input("Sobrenome: ")

tamanho_total = len(nome) + len(sobrenome)
login = nome + sobrenome + str(tamanho_total)

print(f"Login: {login}")