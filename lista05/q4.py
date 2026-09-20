n = int(input("Quantidade de participantes: "))

nomes = []
problemas = []
penalidades = []

for i in range(n):
    print(f"\nParticipante {i+1}")

    nome = input("Nome: ")
    resolvidos = int(input("Problemas resolvidos: "))
    penalidade = int(input("Penalidade: "))

    nomes.append(nome)
    problemas.append(resolvidos)
    penalidades.append(penalidade)

melhor = 0

for i in range(1, n):

    if problemas[i] > problemas[melhor]:
        melhor = i

    elif problemas[i] == problemas[melhor]:

        if penalidades[i] < penalidades[melhor]:
            melhor = i

resolveram = 0

for quantidade in problemas:
    if quantidade > 0:
        resolveram += 1

media_problemas = sum(problemas) / len(problemas)

print("\n--- RESULTADO ---")
print(f"Campeão: {nomes[melhor]}")
print(f"Problemas resolvidos: {problemas[melhor]}")
print(f"Penalidade: {penalidades[melhor]}")

print(f"Participantes que resolveram pelo menos um problema: {resolveram}")
print(f"Média de problemas resolvidos: {media_problemas:.2f}")