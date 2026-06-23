'''
1 cigarro => 10 minutos de vida a menos
x cigarros => 1 dia = 24 * 60min = 1440 minutos
x = 1440 / 10 = 144 cigarros para perder um dia de vida
'''

cigarros_por_dia = int(input('Cigarros por dia: '))
anos_fumados = int(input('Anos que fumou: '))

total_cigarros = anos_fumados * 365 * cigarros_por_dia
dias_perdidos = total_cigarros / 144

print ('Você perdeu aproximadamente %d dias de vida.' % dias_perdidos)

# Calcular na forma ano/dias
anos_fumados = dias_perdidos // 365
dias_fumados = dias_perdidos % 365
print ('Perdeu aproximadamente %d ano(s) e %d dia(s)' % (anos_fumados, dias_fumados))
