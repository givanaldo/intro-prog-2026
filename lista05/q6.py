n = int(input("Quantidade de números: "))

numeros = []

for i in range(n):
    valor = int(input(f"Número {i + 1}: "))
    numeros.append(valor)

inicio_atual = 0
tamanho_atual = 1
melhor_inicio = 0
melhor_tamanho = 1

for i in range(1, n):
    if numeros[i] > numeros[i - 1]:
        tamanho_atual += 1
    else:
        inicio_atual = i
        tamanho_atual = 1
    if tamanho_atual > melhor_tamanho:
        melhor_tamanho = tamanho_atual
        melhor_inicio = inicio_atual

melhor_fim = melhor_inicio + melhor_tamanho - 1

print("\n--- RESULTADO ---")
print(f"Maior sequência crescente: {melhor_tamanho} elementos")
print(f"Início: índice {melhor_inicio}")
print(f"Fim: índice {melhor_fim}")