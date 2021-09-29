import math

num = int(input("Digite um número: "))

if num > 0:
    raiz = math.sqrt(num)
    print("A raiz quadrada de {} é {:.2}".format(num, raiz))