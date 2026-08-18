a = int(input("Lado A: "))
b = int(input("Lado B: "))
c = int(input("Lado C: "))
if a<b+c and b<a+c and c<a+b:
    if a == b == c:
        print("Triângulo Equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo Isóceles.")
    else:
        print("Triângulo Escaleno.")
else:
    print("Os lados não formam um triângulo.")