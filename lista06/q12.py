# Estrutura: LISTA + CONJUNTO
n = int(input("Quantidade de acessos: "))
historico = []

for i in range(n):
    ip = input("IP: ")
    historico.append(ip)

unicos = set(historico)
repetidos = []

for ip in unicos:
    if historico.count(ip) > 1:
        repetidos.append(ip)

print("Total de acessos:", len(historico))
print("IPs diferentes:", len(unicos))
print("IPs repetidos:", sorted(repetidos))
print("IPs únicos:", sorted(unicos))