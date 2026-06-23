tamanho_arquivo_mb = float(input("Tamanho do arquivo (em MB): "))
velocidade_mbps = float(input("Velocidade do seu link de Internet (em Mbps): "))

# 1 Byte = 8 bits, logo multiplicamos os MB por 8 para ter Megabits
tamanho_megabits = tamanho_arquivo_mb * 8  # arquivo em megabits
tempo_segundos = tamanho_megabits / velocidade_mbps
tempo_minutos = tempo_segundos / 60

print(f"O tempo aproximado de descarregamento é de {tempo_minutos:.2f} minutos.")