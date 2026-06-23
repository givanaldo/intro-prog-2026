dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

# Considerando:
# 1 dia = 24 horas
# 1 hora = 60 minutos
# 1 minutos = 60 segundos

total_segundos = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos
print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos = {total_segundos} segundos.")
