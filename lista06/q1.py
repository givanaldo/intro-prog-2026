#Estrutura: LISTA
notas = []
for i in range(1, 9):
    nota = int(input(f"Digite a nota {i}: "))
    notas.append(nota)
print(f"Maior nota: {max(notas)}")
print(f"Menor nota: {min(notas)}")
print(f"Média: {sum(notas) / len(notas):.0f}")

posicao = int(input("Nota a ser alterada (1-8): "))
if posicao >= 1 and posicao <= 8:
    nova_nota = int(input("Nova nota: "))
    notas[posicao-1] = nova_nota
    print(notas)
    print(f"Maior nota: {max(notas)}")
    print(f"Menor nota: {min(notas)}")
    print(f"Média: {sum(notas) / len(notas):.0f}")
else:
    print("Posição inválida!")