n = int(input("Quantidade de vendedores: "))
m = int(input("Quantidade de dias: "))
nomes = []
vendas = []

for i in range(n):
    nome = input(f"\nNome do vendedor {i + 1}: ")
    nomes.append(nome)
    vendas_vendedor = []
    for dia in range(m):
        valor = float(input(f"Venda do dia {dia + 1}: R$ "))
        vendas_vendedor.append(valor)
    vendas.append(vendas_vendedor)
totais = []

for i in range(n):
    total = sum(vendas[i])
    totais.append(total)
    print(f"{nomes[i]} vendeu R$ {total:.2f}")

indice_melhor = 0
for i in range(1, n):
    if totais[i] > totais[indice_melhor]:
        indice_melhor = i
print(f"\nMaior faturamento: {nomes[indice_melhor]}")

totais_dias = []
for dia in range(m):
    total_dia = 0
    for vendedor in range(n):
        total_dia += vendas[vendedor][dia]
    totais_dias.append(total_dia)
melhor_dia = 0

for dia in range(1, m):
    if totais_dias[dia] > totais_dias[melhor_dia]:
        melhor_dia = dia

faturamento_total = sum(totais)

media_diaria = faturamento_total / m

media_vendedor = faturamento_total / n

acima_da_media = 0

for total in totais:
    if total > media_vendedor:
        acima_da_media += 1

print("\n--- RELATÓRIO ---")
print(f"Vendedor com maior faturamento: {nomes[indice_melhor]}")
print(f"Dia de maior faturamento: {melhor_dia + 1}")
print(f"Faturamento total: R$ {faturamento_total:.2f}")
print(f"Média diária: R$ {media_diaria:.2f}")
print(f"Vendedores acima da média: {acima_da_media}")