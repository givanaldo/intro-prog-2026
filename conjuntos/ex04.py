import random
numeros = []
for i in range(101):
    numeros.append(random.randint(0, 100))
print(numeros)
print(f"Número diferentes: {len(set(numeros))}")