# Estrutura: Tupla (não pode modificar depois)
pontos = []
for i in range(1, 4):
    x = float(input(f"X{i}: "))
    y = float(input(f"Y{i}: "))
    pontos.append((x, y))
print("Pontos cadastrados: ")
for p in pontos:
    print(f"- {p}")
for i in range(3):
    x, y = pontos[i]
    if x > 0 and y > 0:
        quadrante = 1
    elif x < 0 and y > 0:
        quadrante = 2
    elif x < 0 and y < 0:
        quadrante = 3
    elif x > 0 and y < 0:
        quadrante = 4
    else:
        quadrante = 0 # ponto sobre um dos eixos
    
    print(f"Ponto {pontos[i]}", end=" ")
    if quadrante == 0:
        print("está sobre um dos eixos.")
    else:
        print(f"está no {quadrante}º quadrante.")