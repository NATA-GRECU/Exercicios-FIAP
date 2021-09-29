salario = float(input("Digite o salário: "))
aumento = float(input("Digite o valor do aumento (%): "))

salario = salario + ((salario * aumento) / 100)

print("O aumento foi de {}%, seu salário agora é de R${} Reais.".format(aumento, salario))