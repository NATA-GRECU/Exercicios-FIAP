anoNascimento = int(input("Digite o ano de nascimento: "))
anoAtual = int(input("Digite o ano atual: "))
idade = anoAtual - anoNascimento

if idade >= 18:
    print("Você tem {} anos ou mais, portando é maior de idade".format(idade))

else:
    print("Você tem menos de {} anos, portando é menor de idade".format(idade))