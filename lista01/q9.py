km_percorridos = float(input('Quilometros percorridos: '))
dias_alugados = int(input('Dias alugados: '))

valor_pagar = 60 * dias_alugados + 0.15 * km_percorridos

print(f'Valor a pagar: R$ {valor_pagar:.2f}')
