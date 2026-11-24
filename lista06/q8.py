# Estrutura: LISTA
temperaturas = []

for i in range(12):
    temp = float(input(f"Temperatura {i + 1}: "))
    temperaturas.append(temp)

media = sum(temperaturas) / len(temperaturas)
maior = max(temperaturas)
indice_maior = temperaturas.index(maior)

acima = 0
for temp in temperaturas:
    if temp > media:
        acima += 1

print(f"Média: {media:.2f}")
print(f"Maior temperatura: {maior}")
print(f"Primeira ocorrência: índice {indice_maior}")
print(f"Leituras acima da média: {acima}")