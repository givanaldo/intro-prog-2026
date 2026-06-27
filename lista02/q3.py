# Entrada de dados
capital = float(input("Valor inicial investido: "))
taxa = float(input("Taxa de juros mensal (em %): "))
meses = int(input("Quantidade de meses: "))

# Processamento
# A fórmula é M = C * (1 + i/100)^t
montante = capital * ((1 + taxa / 100) ** meses)
lucro = montante - capital

# Saída
print(f"O Montante final será de: R$ {montante:.2f}")
print(f"O Lucro gerado pelos juros foi de: R$ {lucro:.2f}")