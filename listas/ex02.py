nomes = ["Maria", "João", "José", "Rosa"]
print(f"Nomes: {nomes}")
while True:
    nome = input("Nome para adicionar: ")
    if nome == "":
        break
    else:
        if nome not in nomes:
            nomes.append(nome)
print(f"Nomes: {nomes}")