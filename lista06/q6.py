# Estrutura: CONJUNTO
robotica = set()
programacao = set()

n = int(input("Alunos da Robótica: "))
for i in range(n):
    robotica.add(input("Nome: "))

n = int(input("Alunos da Programação: "))
for i in range(n):
    programacao.add(input("Nome: "))

print("Nos dois:", sorted(robotica & programacao))
print("Em pelo menos um:", sorted(robotica | programacao))
print("Só Robótica:", sorted(robotica - programacao))
print("Somente um clube:", sorted(robotica ^ programacao))