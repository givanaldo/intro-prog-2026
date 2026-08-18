n1 = int(input("n1: "))
n2 = int(input("n2: "))
print("[1] Somar")
print("[2] Subtrair")
print("[3] Multiplicar")
print("[4] Dividir")
print("[5] Potência")
opcao = int(input("Opção: "))
if opcao == 1:
    resultado = n1 + n2
    print(f">> {n1} + {n2} = {resultado}")
elif opcao == 2:
    resultado = n1 - n2
    print(f">> {n1} - {n2} = {resultado}")
elif opcao == 3:
    resultado = n1 * n2
    print(f">> {n1} * {n2} = {resultado}")
elif opcao == 4:
    resultado = n1 / n2
    print(f">> {n1} / {n2} = {resultado}")
elif opcao == 5:
    resultado = n1 ** n2
    print(f">> {n1} ** {n2} = {resultado}")
else:
    print("Opção inválida!")
