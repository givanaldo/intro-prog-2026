n = int(input("Quantidade de alunos: "))

medias = []

aprovados = 0
prova_final = 0
reprovados = 0

for aluno in range(1, n+1):
    print(f"\nAluno {aluno}")

    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))

    media = (nota1 + nota2) / 2

    medias.append(media)

    if media >= 60:
        aprovados += 1
        situacao = "Aprovado"

    elif media >= 20:
        prova_final += 1
        situacao = "Prova Final"

    else:
        reprovados += 1
        situacao = "Reprovado"

    print(f"Média: {media:.0f}")
    print(f"Situação: {situacao}")

media_geral = sum(medias) / len(medias)
percentual_aprovados = aprovados / n * 100

print("\n--- RELATÓRIO ---")
print(f"Maior média: {max(medias):.0f}")
print(f"Menor média: {min(medias):.0f}")
print(f"Média geral: {media_geral:.0f}")

print(f"Aprovados: {aprovados}")
print(f"Prova Final: {prova_final}")
print(f"Reprovados: {reprovados}")

print(f"Percentual de aprovados: {percentual_aprovados:.1f}%")

print("Médias em ordem decrescente:")
print(sorted(medias, reverse=True))