# Entrada de dados
a = int(input("Valor numérico de A: "))
b = int(input("Valor numérico de B: "))

print(f"Antes da troca: A = {a}, B = {b}")

# Processamento - O truque matemático
a = a + b  # 'a' agora contém a soma de ambos
b = a - b  # Subtraindo o valor original de 'b' da soma, obtemos o valor original de 'a'
a = a - b  # Subtraindo o NOVO 'b' (que é o antigo 'a') da soma, obtemos o antigo 'b'

# Saída
print(f"Depois da troca: A = {a}, B = {b}")