''' Algoritmo de Euclides para MDC
- Divida o número maior (a) pelo menor (b) 
- Encontre o resto (r) dessa divisão.
- Substitua o número maior pelo divisor anterior (b), e o divisor pelo resto (r).
- Repita a divisão até que o resto seja zero.
- O último resto diferente de zero é o MDC.
'''
num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
if num2 > num1:
    num1, num2 = num2, num1
while num2 != 0:
    resto = num1 % num2
    num1 = num2
    num2 = resto
print(f"MDC = {num1}")