num1 = float(input("Digite o valor para o 1º número: "))
operacao = input("Digite o sinal da operação desejada: ")
num2 = float(input("Digite o valor para o 2º número: "))

if operacao == '+':
    resultado = num1 + num2
    print("A soma de {} e {}, resulta em {}".format(num1,num2,resultado))

elif operacao == '-':
    resultado = num1 - num2
    print("A subtração de {} e {}, resulta em {}".format(num1, num2, resultado))

elif operacao == '*':
    resultado = num1 * num2
    print("A multiplicação de {} e {}, resulta em {}".format(num1, num2, resultado))

elif operacao == '/':
    resultado = float(num1 / num2)
    print("A divisão de {} e {}, resulta em {}".format(num1, num2, resultado))

else:
    print("Operação desconhecida!")