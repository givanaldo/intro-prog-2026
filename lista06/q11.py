# Estrutura: LISTA + TUPLA
resultados = []

for i in range(6):
    resultado = input(f"Teste {i + 1} (OK/FALHA): ").upper()
    resultados.append(resultado)

relatorio = tuple(resultados)

passaram = relatorio.count("OK")
falharam = relatorio.count("FALHA")

print("Relatório:", relatorio)
print("Passaram:", passaram)
print("Falharam:", falharam)

if "FALHA" in relatorio:
    print("Primeira falha: posição", relatorio.index("FALHA") + 1)
else:
    print("Nenhuma falha.")