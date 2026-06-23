pessoas = int(input("Para quantas pessoas deseja fazer o bolo? "))

# A receita original é para 4 pessoas, logo encontramos o fator multiplicador)
fator = pessoas / 4
ovos = 3 * fator
farinha = 2 * fator
acucar = 1.5 * fator

print(f"\nPara servir {pessoas} pessoas, precisará de:")
print(f"{ovos} ovos")
print(f"{farinha} xícaras de farinha")
print(f"{acucar} xícaras de açúcar")