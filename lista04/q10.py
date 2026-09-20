nome = input("Nome: ")

lista = ["João", "Pedro", "Ana", "Maria", "Alex", 
         "Rosa", "Julia", "Alexa", "Silvia", "Marlon",
         "Rossana", "Pedro", "Lucia", "Amaral", "Jobson", 
         "Carlos", "Lorena", "Rosy", "Judson", "Bruno"]

if nome in lista:
    print(f"{nome} consta na lista.")
else:
    print(f"{nome} não consta na lista.")