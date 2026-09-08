ano = int(input("Ano para o projeto especial: "))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("O ano é bissexto, teremos Projeto Especial!")
else:
    print("Não teremos Projeto Especial!")
