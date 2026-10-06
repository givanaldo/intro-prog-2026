estoque = 100

maior_estoque = estoque
menor_estoque = estoque

n = int(input("Quantidade de operações no dia: "))

estoque_negativo = False

for op in range(1, n+1):
    movimento = int(input(f"Movimentação {op}: "))

    estoque = estoque + movimento

    if estoque > maior_estoque:
        maior_estoque = estoque

    if estoque < menor_estoque:
        menor_estoque = estoque

    if estoque < 0:
        print(f"\nEstoque negativo na operação {op}.")
        print(f"Estoque no momento do erro: {estoque}")
        estoque_negativo = True
        break

print(f"Maior estoque registrado: {maior_estoque}")
print(f"Menor estoque registrado: {menor_estoque}")

if not estoque_negativo:
    print(f"Estoque final: {estoque}")