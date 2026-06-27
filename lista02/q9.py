# Entrada de dados
dia_atual = int(input("Qual é o dia atual? (0=Dom, 1=Seg... 6=Sáb): "))
dias_espera = int(input("Quantos dias vai aguardar? "))

# Processamento
# O operador módulo (%) resolve o problema do ciclo infinito dos 7 dias da semana
dia_futuro = (dia_atual + dias_espera) % 7

# Saída
print(f"Após {dias_espera} dias, o evento cairá no dia da semana número {dia_futuro}.")