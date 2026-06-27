# Entrada de dados
numero = int(input("Número inteiro de 3 dígitos (ex: 485): "))

# Processamento
centenas = numero // 100
resto = numero % 100
dezenas = resto // 10
unidades = resto % 10

# Reconstruindo o número invertido matematicamente
numero_invertido = (unidades * 100) + (dezenas * 10) + centenas

# Saída
print(f"Centenas: {centenas}")
print(f"Dezenas: {dezenas}")
print(f"Unidades: {unidades}")
print(f"O número invertido é: {numero_invertido}")