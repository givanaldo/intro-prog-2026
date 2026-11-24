# Estrutura: LISTA DE TUPLAS
n = int(input("Quantidade de participantes: "))
classificacao = []

for i in range(n):
    nome = input("Nome: ")
    pontos = int(input("Pontuação: "))
    classificacao.append((nome, pontos))

maior = classificacao[0][1]

for participante in classificacao:
    if participante[1] > maior:
        maior = participante[1]

campeoes = []

for participante in classificacao:
    if participante[1] == maior:
        campeoes.append(participante[0])

print("Maior pontuação:", maior)
print("Primeiro lugar:")

for nome in campeoes:
    print(nome)