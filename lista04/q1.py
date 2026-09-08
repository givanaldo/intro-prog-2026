nota = int(input("Nota (0 a 10): "))
while nota < 0 or nota > 10:
    print("Nota inválida!")
    nota = int(input("Nota (0 a 10): "))
print(f'Nota válida digitada: {nota}')    
