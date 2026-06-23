largura = float(input("Largura da parede (m): "))
altura = float(input("Altura da parede (m): "))

area_total = largura * altura
litros_tinta = area_total / 3

print(f"A área total da parede é de {area_total} m².")
print(f"Serão necessários {litros_tinta:.2f} litros de tinta para a pintura.")