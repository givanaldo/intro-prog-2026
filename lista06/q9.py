# Estrutura: LISTA DE TUPLAS + CONJUNTO
n = int(input("Quantidade de posições: "))
caminho = []

for i in range(n):
    x = int(input("x: "))
    y = int(input("y: "))
    caminho.append((x, y))

visitados = set(caminho)

print("Primeiro ponto:", caminho[0])
print("Último ponto:", caminho[-1])
print("Posições registradas:", len(caminho))
print("Posições diferentes:", len(visitados))