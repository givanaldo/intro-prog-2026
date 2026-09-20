num = int(input('Digite um número: '))

resultado = ""
fator = 2
quociente = num

while quociente != 1:
    if quociente % fator == 0:
        quociente = quociente // fator
        resultado = resultado + "%d x " % fator
    else:
        fator += 1

print(resultado[:-2])
