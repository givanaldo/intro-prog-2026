saldo = float(input("Saldo inicial: R$ "))
n = int(input("Quantidade de transações: "))

transacoes_suspeitas = []

retiradas_consecutivas = 0

for i in range(1, n+1):
    valor = float(input(f"Transação {i}: R$ "))

    saldo += valor

    suspeita = False

    # Regra 1: valor absoluto maior que 5000
    if abs(valor) > 5000:
        suspeita = True

    # Regra 2: saldo negativo
    if saldo < 0:
        suspeita = True

    # Controla retiradas consecutivas
    if valor < 0:
        retiradas_consecutivas += 1
    else:
        retiradas_consecutivas = 0

    # Regra 3: três ou mais retiradas seguidas
    if retiradas_consecutivas >= 3:
        suspeita = True

    if suspeita:
        transacoes_suspeitas.append(i)

print("\n--- RELATÓRIO ---")
print(f"Saldo final: R$ {saldo:.2f}")
print(f"Quantidade de transações suspeitas: {len(transacoes_suspeitas)}")

print("Transações suspeitas:", transacoes_suspeitas)