conta = float(input("Valor total da conta: "))
pessoas = int(input("Quantidade de pessoas na mesa: "))

conta_com_gorjeta = conta * 1.10 # ou conta + conta * 0.10
valor_por_pessoa = conta_com_gorjeta / pessoas

print(f"Valor total com gorjeta é R$ {conta_com_gorjeta:.2f}")
print(f"Cada pessoa deve pagar: R$ {valor_por_pessoa:.2f}")