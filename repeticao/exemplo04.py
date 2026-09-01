texto = "O rato roeu a roupa do rei de Roma"
vogais = "AEIOUÁÃÂÉÊÍÓÔÕÚ"
n = 0
for letra in texto:
    if letra.upper() in vogais:
        n = n + 1
print(f"Vogais: {n}")
        