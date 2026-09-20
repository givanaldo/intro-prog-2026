n = int(input("Digite um número: "))
i = 1
while i * (i + 1) * (i + 2) < n:
    i += 1
if i * (i + 1) * (i + 2) == n:
    print(f"O número {n} é triangular, pois {i} * {i+1} * {i+2} = {n}")
else:
    print(f"O número {n} não é triangular.")