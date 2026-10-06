conta = int(input('Valor da conta: '))
pagamento = int(input('Valor do pagamento: '))
troco = pagamento - conta
notas = [50, 20, 10, 5, 2, 1]
print(f"Troco: R$ {troco}")
for nota in notas:
    num_notas = troco // nota
    if num_notas != 0:
        print(f"   -- {num_notas} nota(s) de {nota}")
    troco = troco % nota
