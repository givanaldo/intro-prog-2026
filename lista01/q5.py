preco_mercadoria = float(input('Preço da mercadoria: '))
porcentagem_desconto = float(input('Porcentagem de desconto: '))

valor_desconto = preco_mercadoria * (porcentagem_desconto / 100)
novo_preco_mercadoria = preco_mercadoria - valor_desconto

print(f'Valor do desconto: R$ {valor_desconto:.2f}')
print(f'Valor a pagar: R$ {novo_preco_mercadoria:.2f}')
