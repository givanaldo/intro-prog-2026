capacidade = int(input("Capacidade do ônibus: "))
n = int(input("Quantidade de paradas: "))

passageiros = 0
maior_lotacao = 0
nao_embarcaram = 0

primeira_lotacao_maxima = 0

for parada in range(1, n + 1):

    print(f"\nParada {parada}")

    sairam = int(input("Quantidade que saiu: "))
    entraram = int(input("Quantidade tentando entrar: "))

    passageiros -= sairam

    vagas = capacidade - passageiros

    if entraram <= vagas:
        passageiros += entraram

    else:
        passageiros = capacidade

        ficaram = entraram - vagas
        nao_embarcaram += ficaram

    if passageiros > maior_lotacao:
        maior_lotacao = passageiros

    if passageiros == capacidade and primeira_lotacao_maxima == 0:
        primeira_lotacao_maxima = parada

print("\n--- RELATÓRIO ---")

print(f"Maior lotação: {maior_lotacao}")
print(f"Não conseguiram embarcar: {nao_embarcaram}")
print(f"Passageiros no fim da viagem: {passageiros}")

if primeira_lotacao_maxima == 0:
    print("O ônibus não atingiu sua capacidade máxima.")
else:
    print(
        f"Primeira parada com lotação máxima: "
        f"{primeira_lotacao_maxima}"
    )