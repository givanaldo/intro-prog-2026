instagram = {"Nathalya", "Leticia", "Kaio", "Sophia",
             "Maria Isabella", "Enzo"}
tiktok = {"Nathalya", "Leticia", "Mirela", "Nicholas", 
          "Maria Isabella", "Luana"}
print(f"Instagram: {instagram - tiktok}")
print(f"Tiktok: {tiktok - instagram}")
print(f"Ambos: {instagram & tiktok}")
print(f"Usa um, mas não ambos: {instagram ^ tiktok}")
