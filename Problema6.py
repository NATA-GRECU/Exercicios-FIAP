timeA = int(input("Digite quantos gols o Time A fez: "))
timeB = int(input("Digite quantos gols o Time B fez: "))

if timeA > timeB:
    print("O Time A ganhou de {} x {}".format(timeA,timeB))

elif timeA == timeB:
    print("O jogo empatou em {} x {}".format(timeA, timeB))

else:
    print("O Time B ganhou de {} x {}".format(timeB,timeA))