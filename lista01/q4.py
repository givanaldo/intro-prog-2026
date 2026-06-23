salario = float(input('Salário: '))
porcentagem = float(input('Porcentagem de aumento: '))

aumento = salario * (porcentagem / 100)
novo_salario = salario + aumento

print(f'Valor do aumento: R$ {aumento:.2f}')
print(f'Novo salário: R$ {novo_salario:.2f}')
