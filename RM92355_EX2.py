qtdTransacoes = int(input("Informe quantas transações você realizou hoje: "))
total = 0

for x in range(1, qtdTransacoes + 1):
    print("Digite o valor da {}º transação: ".format(x))
    valor = float(input(""))

    total = total + valor

mediaTransacoes = total / qtdTransacoes
print("A média de cada transação foi de R$ {} reais.".format(mediaTransacoes))
print("O valor total dos gastos do dia é de R$ {} reais.".format(total))
