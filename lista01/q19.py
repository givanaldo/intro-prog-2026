horas_livres = float(input("Horas livres por semana: "))
qtd_disciplinas = int(input("Disciplinas a cursar: "))

horas_disponiveis_estudo = horas_livres - 3
horas_por_disciplina = horas_disponiveis_estudo / qtd_disciplinas

print(f"Descontando os imprevistos, tem {horas_disponiveis_estudo} horas líquidas.")
print(f"Deve dedicar {horas_por_disciplina:.2f} horas por semana para cada disciplina.")