# Estrutura: CONJUNTO
projeto_a = {"Python", "Git", "Linux", "Docker"}
projeto_b = {"Python", "Git", "JavaScript", "SQL"}

print("Em comum:", projeto_a & projeto_b)
print("Em pelo menos um:", projeto_a | projeto_b)
print("Só no A:", projeto_a - projeto_b)
print("Só no B:", projeto_b - projeto_a)
print("Em apenas um projeto:", projeto_a ^ projeto_b)