saldo = int(input("Saldo de moedas: "))
valor_skin = int(input("Valor da skin: "))

if saldo >= valor_skin:
    print("Compra realizada! Aproveite sua nova skin.")
    saldo = saldo - valor_skin
    print(f"Saldo restante de {saldo} moedas")
else:
    print("Saldo insuficiente! ")
    restante = valor_skin - saldo
    print(f"Faltam {restante} moedas para comprar este item.")