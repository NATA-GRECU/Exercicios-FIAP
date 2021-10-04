qtdAlimentos = int(input("Digite a quantos alimentos você consumiu hoje: "))
totalCalorias = 0

for x in range(1,qtdAlimentos+1):
    print("Digite quantas calorias tem o {}º alimento: ".format(x))
    calorias = float(input(""))
    totalCalorias = totalCalorias + calorias

print("O total de calorias consumidas hoje foi de {} Kcal.".format(totalCalorias))
