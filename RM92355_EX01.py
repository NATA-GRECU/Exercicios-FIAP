peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura * altura)

if imc < 16:
    print("Seu IMC é: Baixo Peso Grau III")

elif imc < 16.99:
    print("Seu IMC é: Baixo Peso Grau II")

elif imc < 18.49:
    print("Seu IMC é: Baixo Peso Grau I")

elif imc < 24.99:
    print("Seu IMC é: Peso Ideal")

elif imc < 29.99:
    print("Seu IMC é: Sobrepeso")

elif imc < 34.99:
    print("Seu IMC é: Obesidade Grau I")

elif imc < 39.99:
    print("Seu IMC é: Obesidade Grau II")

else:
    print("Seu IMC é: Obesidade Grau III")