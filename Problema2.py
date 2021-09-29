salario = float(input("Digite o salário: "))
aumento = float(input("Digite o valor do aumento (%): "))
cargo = input("Digite o cargo: ")

salario = salario + ((salario * aumento) / 100)

if cargo.lower() == "gerente":
    salario = salario + ((salario * 1.5) / 100)

print("O aumento foi de {}%, seu salário agora é de R${} Reais.".format(aumento, salario))