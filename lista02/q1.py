# Entrada de dados
total_segundos = int(input("Total de segundos: "))

# Processamento
# 1 dia = 24h * 60m * 60s = 86400 segundos
dias = total_segundos // 86400
resto_segundos = total_segundos % 86400

# 1 hora = 3600 segundos
horas = resto_segundos // 3600
resto_segundos = resto_segundos % 3600

# 1 minuto = 60 segundos
minutos = resto_segundos // 60
segundos = resto_segundos % 60

# Saída
print(f"{total_segundos} segundos ==> {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")