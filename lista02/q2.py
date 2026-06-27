# Entrada de dados
valor = int(input("Valor que deseja levantar: R$ "))

# Processamento
notas_100 = valor // 100
resto = valor % 100

notas_50 = resto // 50
resto = resto % 50

notas_20 = resto // 20
resto = resto % 20

notas_10 = resto // 10
resto = resto % 10

notas_5 = resto // 5
resto = resto % 5

notas_2 = resto // 2
notas_1 = resto % 2 # O último resto são as moedas/notas de 1

# Saída
print(f"Notas de 100: {notas_100}")
print(f"Notas de 50: {notas_50}")
print(f"Notas de 20: {notas_20}")
print(f"Notas de 10: {notas_10}")
print(f"Notas de 5: {notas_5}")
print(f"Notas de 2: {notas_2}")
print(f"Notas/Moedas de 1: {notas_1}")