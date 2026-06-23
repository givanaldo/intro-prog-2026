peso = float(input("Peso (em kg): "))
altura = float(input("Altura (em metros): "))

imc = peso / (altura ** 2)

print(f"Índice de Massa Corporal (IMC): {imc:.2f}")