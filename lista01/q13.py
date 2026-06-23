reais = float(input("Reais economizados: R$ "))
cotacao = float(input("Cotação atual do Dólar: R$ "))

dolares = reais / cotacao

print(f"Com R$ {reais:.2f}, conseguirá comprar US$ {dolares:.2f}.")