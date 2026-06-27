# Entrada de dados
distancia = float(input("Qual a distância total entre as duas cidades (em km)? "))

# Processamento
# Como estão em sentidos opostos, as velocidades somam-se para o cálculo do tempo
velocidade_a = 80
velocidade_b = 100
velocidade_relativa = velocidade_a + velocidade_b
tempo_horas = distancia / velocidade_relativa

# Saída
print(f"Os amigos vão cruzar-se na estrada após {tempo_horas:.2f} horas.")