# (x1, y1) (x2, y2) (x3, y3) - tuplas
pontos = []
i = 1
while i <= 3:
    x = float(input(f"X{i}: "))
    y = float(input(f"Y{i}: "))
    i = i + 1
    pontos.append((x, y))

print(pontos)

'''
for p in pontos:
    print(p, end=" - ")
    x, y = p
    if x > 0 and y > 0:
        print("1º Quadrante")
    elif x < 0 and y > 0:
        print("2º Quadrante")
    elif x < 0 and y < 0:
        print("3º Quadrante")
    elif x > 0 and y < 0:
        print("4º Quadrante")
    else:
        print("Ponto está em um dos eixos")
'''    
