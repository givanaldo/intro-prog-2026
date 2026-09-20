# Um número é primo se é divisível apenas por ele mesmo e por 1.
# Só faz sentido testar da metade do número para trás, pois
# acima já se tem certeza que não é divisível, além dele mesmo.

num = int(input('Digite um número: '))

é_primo = True
for i in range(2, (num//2)+1):
    if num % i == 0:
        é_primo = False
        break

if é_primo == True:
    print(f"O número {num} é primo.")
else:
    print(f"O número {num} não é primo.")
