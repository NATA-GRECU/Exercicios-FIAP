salario = float(input("Digite seu salário: R$ "))

if salario <= 1693.72:
    print("Seu salário é de R${}, logo sofrerá um desconto de 8%".format(salario))

elif salario <= 2822.90:
    print("Seu salário é de R${}, logo sofrerá um desconto de 9%".format(salario))

elif salario <= 5646.80:
    print("Seu salário é de R${}, logo sofrerá um desconto de 11%".format(salario))

else:
    print("Seu salário é de R${}, logo sofrerá um desconto de 11% sobre o teto da aposentadoria".format(salario))