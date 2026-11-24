# Estrutura: LISTA DE TUPLAS + CONJUNTO
n = int(input("Quantidade de posições: "))
rota = []

for i in range(n):
    x = int(input("x: "))
    y = int(input("y: "))
    rota.append((x, y))

unicas = set(rota)
vistos = set()
revisitadas = set()
primeira_revisita = None

for ponto in rota:
    if ponto in vistos:
        revisitadas.add(ponto)
        if primeira_revisita is None:
            primeira_revisita = ponto
    else:
        vistos.add(ponto)

print("Rota:", rota)
print("Posições registradas:", len(rota))
print("Posições diferentes:", len(unicas))
print("Posições revisitadas:", sorted(revisitadas))

if primeira_revisita is None:
    print("Nenhuma posição foi revisitada.")
else:
    print("Primeira posição revisitada:", primeira_revisita)