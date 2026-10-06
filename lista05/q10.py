n = int(input("Quantidade de robôs: "))
m = int(input("Quantidade de provas: "))
nomes = []
pontos = []

for i in range(n):
    nome = input(f"\nNome do robô {i + 1}: ")
    nomes.append(nome)
    notas_robo = []
    for prova in range(m):
        nota = int(input(f"Nota na prova {prova + 1}: "))
        notas_robo.append(nota)
    pontos.append(notas_robo)

totais = []
medias = []
notas_10 = []

for i in range(n):
    total = sum(pontos[i])
    media = total / m
    quantidade_10 = pontos[i].count(10)
    totais.append(total)
    medias.append(media)
    notas_10.append(quantidade_10)

print("\n--- RESULTADOS DOS ROBÔS ---")

for i in range(n):
    print(f"\n{nomes[i]}")
    print(f"Total: {totais[i]}")
    print(f"Média: {medias[i]:.2f}")
    print(f"Notas 10: {notas_10[i]}")
    
melhor_total = max(totais)
melhor_qtd_10 = -1

for i in range(n):
    if totais[i] == melhor_total:
        if notas_10[i] > melhor_qtd_10:
            melhor_qtd_10 = notas_10[i]

campeoes = []

for i in range(n):
    if totais[i] == melhor_total and notas_10[i] == melhor_qtd_10:
        campeoes.append(nomes[i])

print("\nCampeão(ões):")

for nome in campeoes:
    print(nome)
    
medias_provas = []

for prova in range(m):
    soma = 0
    for robo in range(n):
        soma += pontos[robo][prova]
    media = soma / n
    medias_provas.append(media)

melhor_prova = 0

for i in range(1, m):
    if medias_provas[i] > medias_provas[melhor_prova]:
        melhor_prova = i

print(f"Prova com maior média: {melhor_prova + 1}")

medias_provas = []

for prova in range(m):
    soma = 0
    for robo in range(n):
        soma += pontos[robo][prova]
    media = soma / n
    medias_provas.append(media)

melhor_prova = 0

for i in range(1, m):
    if medias_provas[i] > medias_provas[melhor_prova]:
        melhor_prova = i

print(f"Prova com maior média: {melhor_prova + 1}")

total_notas_10 = sum(notas_10)

print(f"Quantidade total de notas 10: {total_notas_10}")