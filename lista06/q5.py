# Estrutura: TUPLA
r = int(input("Vermelho: "))
g = int(input("Verde: "))
b = int(input("Azul: "))

if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
    cor = (r, g, b)
    r, g, b = cor
    print(f"RGB({r}, {g}, {b})")
else:
    print("Componente inválido.")