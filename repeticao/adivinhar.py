palavra_correta = "sexta"

while True:
    palavra = input("Palavra: ")
    if palavra != palavra_correta:
        print("Errouuu!!! Tente novamente!")
    else:
        print("Acertou! Parabéns!")
        break

print("Obrigado por participar!")
