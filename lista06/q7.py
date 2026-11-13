# Estrutura: LISTA + CONJUNTO
n = int(input("Quantidade de leituras: "))
leituras = []

for i in range(n):
    codigo = int(input("Código: "))
    leituras.append(codigo)

distintos = set(leituras)

print("Leituras:", leituras)
print("Quantidade de códigos distintos:", len(distintos))
print("Sem duplicatas:", sorted(distintos))