eventos = [4, 4, 4, 2, 2, 8, 8, 8, 8, 3]
codigos = []
quantidades = []

codigo_atual = eventos[0]
contador = 1

for i in range(1, len(eventos)):
    if eventos[i] == codigo_atual:
        contador += 1
    else:
        codigos.append(codigo_atual)
        quantidades.append(contador)
        codigo_atual = eventos[i]
        contador = 1

codigos.append(codigo_atual)
quantidades.append(contador)

indice_maior = quantidades.index(max(quantidades))

print(f"Atividades: {eventos}")
print(f"Códigos: {codigos}")
print(f"Quantidades: {quantidades}")
print(f"Maior sequência: código {codigos[indice_maior]}")
print(f"Quantidade consecutiva: {quantidades[indice_maior]}")