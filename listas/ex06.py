nomes = ["Maria", "João", "José", "Rosa", "José", "Zé"]
nome = input("Nome: ")
if nome in nomes:
    posicao = nomes.index(nome)
    print(f"Posição de {nome} na lista: {posicao}.")
else:
    print(f"{nome} não está na lista.")