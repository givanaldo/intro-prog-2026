quantidade_horas = float(input("Quantidade de horas por dia: "))
if quantidade_horas < 1:
    print("Expectador casual.")
elif quantidade_horas <= 3:
    print("Maratonista iniciante.")
elif quantidade_horas <= 5:
    print("Maratonista profissional.")
else:
    print("Alerta Vermelho! Desligue a tela e vá ver o sol!")