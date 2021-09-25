# Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver
# um trabalho em parceria: um serviço em que as pessoas possam usar um estúdio profissional
# para gravar seus vídeos para o YouTube com máxima qualidade. O serviço ganha dinheiro por
# meio de um sistema de assinaturas e de um bônus calculado por uma porcentagem sobre o
# faturamento que o canal do cliente obteve ao longo do ano.
# Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento
# anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês.
# A tabela abaixo mostra a porcentagem de acordo com cada nível de assinatura:

assinatura = input("Digite o tipo de assinatura: ")
faturamentoAnual = float(input("Digite seu faturamento anual: "))

if assinatura.lower() == "basic":
    valorBonus = (faturamentoAnual * 30) / 100
    print("Você deverá pagar R${} de bônus.".format(valorBonus))

elif assinatura.lower() == "silver":
    valorBonus = (faturamentoAnual * 20) / 100
    print("Você deverá pagar R${} de bônus.".format(valorBonus))

elif assinatura.lower() == "gold":
    valorBonus = (faturamentoAnual * 10) / 100
    print("Você deverá pagar R${} de bônus.".format(valorBonus))

elif assinatura.lower() == "platinum":
    valorBonus = (faturamentoAnual * 5) / 100
    print("Você deverá pagar R${} de bônus.".format(valorBonus))

else:
    print("Esse tipo de assinatura não existe")