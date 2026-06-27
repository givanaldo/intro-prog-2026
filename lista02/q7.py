# Entrada de dados
valor_hora = float(input("Quanto ganha por hora? R$ "))
horas_trabalhadas = float(input("Quantas horas trabalhou no mês? "))

# Processamento (A ordem das operações é fundamental aqui)
salario_bruto = valor_hora * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

# O líquido é o bruto subtraído do somatório dos descontos
salario_liquido = salario_bruto - (ir + inss + sindicato)

# Saída
print(f"+ Salário Bruto : R$ {salario_bruto:.2f}")
print(f"- IR (11%) : R$ {ir:.2f}")
print(f"- INSS (8%) : R$ {inss:.2f}")
print(f"- Sindicato (5%) : R$ {sindicato:.2f}")
print(f"= Salário Líquido : R$ {salario_liquido:.2f}")