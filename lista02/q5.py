# Entrada de dados
x1 = float(input("Coordenada X do Drone 1: "))
y1 = float(input("Coordenada Y do Drone 1: "))
x2 = float(input("Coordenada X do Drone 2: "))
y2 = float(input("Coordenada Y do Drone 2: "))

# Processamento
# Elevar a 0.5 para calcular a raiz quadrada sem precisar de importar a biblioteca math
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Saída
print(f"A distância em linha reta entre os drones é de {distancia:.2f} unidades.")