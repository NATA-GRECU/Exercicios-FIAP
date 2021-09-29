preco = float(input("Digite o valor do produto: R$ "))
cod = input("Digite o código para pagamento: ")

if cod == '1':
    desconto = (preco * 0.10)
    valorFinal = preco - desconto
    print("Compra realizada no valor R${} , com desconto de R${}.\nCódigo de pagamento {}"
          .format(valorFinal, desconto,cod))

elif cod == '2':
    desconto = (preco * 0.05)
    valorFinal = preco - desconto
    print("Compra realizada no valor R${} , com desconto de R${}.\nCódigo de pagamento {}"
          .format(valorFinal, desconto,cod))

elif cod == '3':
    parcelas = preco / 2
    print("Compra realizada no valor R${}, em 2X de R${} ao mês.\nCódigo de pagamento {}"
          .format(preco, parcelas,cod))

elif cod == '4':
    juros = (preco * 0.07)
    valorFinal = preco + juros
    parcelas = valorFinal / 4
    print("Compra realizada no valor R${}, em 4X de R${} ao mês, com juros de R${}.\nCódigo de pagamento {}"
          .format(valorFinal, parcelas,juros,cod))

else:
    print("Operação não identificada.")