tanque = float(input("Capacidade do tanque do carro (em litros)? "))
consumo = float(input("Consumo médio do carro (km/l)? "))
preco_gasolina = float(input("Preço atual do litro da gasolina? R$ "))

distancia_maxima = tanque * consumo
custo_total = tanque * preco_gasolina

print(f"A distância máxima que o carro consegue percorrer é de {distancia_maxima} km.")
print(f"O custo para encher o tanque completamente será de R$ {custo_total:.2f}.")