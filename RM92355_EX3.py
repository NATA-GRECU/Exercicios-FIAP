i = 0
anterior = 0
n = 1
proximo = 0
sequencia = [n]

while i <= 100:
   proximo = anterior + n
   anterior = n
   n = proximo
   i = i + 1
   sequencia.append(proximo)

valor = int(input("Digite um valor númerico existente na sequência de Fibonacci: "))

if sequencia.__contains__(valor):
   print("Ação bem sucedida!")
else:
   print("A ação falhou...")
