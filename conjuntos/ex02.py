nomes = {"Bia", "Jô", "Zé"}
nomes.add("João")
nomes.add("Zé")
novos = ["Mary", "Zoe", "Lu"]
nomes.update(novos)
print(sorted(nomes))
print(sorted(nomes, reverse=True))