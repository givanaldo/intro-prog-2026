# O aluno teve que isolar a Prova 3 na fórmula:
# (P1*2 + P2*3 + P3*5) / 10 = 7.0
# P1*2 + P2*3 + P3*5 = 70
# P3*5 = 70 - (P1*2 + P2*3)
# P3 = (70 - (P1*2 + P2*3)) / 5

# Entrada de dados
p1 = float(input("Nota da Prova 1: "))
p2 = float(input("Nota da Prova 2: "))

# Processamento
nota_necessaria = (70 - (p1 * 2 + p2 * 3)) / 5

# Saída
print(f"Para atingir a média 7.0, precisará de tirar {nota_necessaria:.1f} na Prova 3.")