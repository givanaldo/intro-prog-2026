linhas = int(input("Linhas: "))
colunas = int(input("Colunas: "))

temperaturas = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        temp = float(input(f"Temperatura [{i}][{j}]: "))
        linha.append(temp)
    temperaturas.append(linha)

maior = temperaturas[0][0]
menor = temperaturas[0][0]

linha_maior = 0
coluna_maior = 0

total = 0
criticos = 0

melhor_media_linha = None
linha_melhor_media = 0

for i in range(linhas):
    soma_linha = 0
    for j in range(colunas):
        temp = temperaturas[i][j]
        total += temp
        soma_linha += temp
        if temp > maior:
            maior = temp
            linha_maior = i
            coluna_maior = j
        if temp < menor:
            menor = temp
        if temp < 15 or temp > 35:
            criticos += 1
    media_linha = soma_linha / colunas

    if melhor_media_linha is None or media_linha > melhor_media_linha:
        melhor_media_linha = media_linha
        linha_melhor_media = i

media = total / (linhas * colunas)

print("\n--- RELATÓRIO ---")
print(f"Maior temperatura: {maior}")
print(f"Posição: [{linha_maior}][{coluna_maior}]")
print(f"Menor temperatura: {menor}")
print(f"Temperatura média: {media:.2f}")
print(f"Sensores críticos: {criticos}")
print(f"Linha com maior média: {linha_melhor_media}")