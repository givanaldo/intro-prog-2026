# Estrutura: CONJUNTO
lista = ["José", "Inácio", "Rosa", "José", "Maria",
         "Maria", "Maria", "José", "Carlos", "Alex"]
inscritos = set(lista)
print(f"Quantidade de inscrições: {len(lista)}")
print(f"Pessoas inscritas: {len(inscritos)}")
print(sorted(inscritos))