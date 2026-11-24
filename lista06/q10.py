# Estrutura: TUPLA + CONJUNTO
reservados = set()
while True:
    fila = int(input("Fila (0 encerra): "))
    if fila == 0:
        break
    coluna = int(input("Coluna: "))
    assento = (fila, coluna)
    if assento in reservados:
        print("Assento já reservado.")
    else:
        reservados.add(assento)
        print("Reserva realizada.")

print("Quantidade de reservas:", len(reservados))
for assento in sorted(reservados):
    print(assento)