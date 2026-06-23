distancia = float(input("Distância da viagem (em km): "))
tempo = int(input("Duração da viagem (em minutos): "))

valor_total = 4.00 + (1.50 * distancia) + (0.25 * tempo)

print(f"O valor total a pagar pela corrida é: R$ {valor_total:.2f}")