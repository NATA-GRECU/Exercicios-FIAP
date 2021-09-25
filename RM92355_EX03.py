#Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor
# para a realização das lives. Desenvolva um programa em que o usuário informe a quantidade
# de votos que cada um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira,
# quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido.

# Lembre-se que padronização e organização são duas características fundamentais para um
# desenvolvedor de sistemas, por isso, fique atento ao formato de entrega da sua atividade:
# cada um dos exercícios deve estar em um script em Python nomeados como: RM?????_EX01.py, RM?????_EX02.py
# e RM?????_EX03.py, sendo que as interrogações devem ser substituídas pelo número do seu RM.

segunda = int(input("Digite a quantidade de votos para segunda-feria: "))
terca = int(input("Digite a quantidade de votos para terça-feria: "))
quarta = int(input("Digite a quantidade de votos para quarta-feria: "))
quinta = int(input("Digite a quantidade de votos para quinta-feria: "))
sexta = int(input("Digite a quantidade de votos para sexta-feria: "))
semEmpate = True

print("\n-----------VOTOS---------------")
print("Segunda-feira: {}".format(segunda))
print("Terça-feira: {}".format(terca))
print("Quarta-feira: {}".format(quarta))
print("Quinta-feira: {}".format(quinta))
print("Sexta-feira: {}".format(sexta))
print("--------------------------------")


if segunda == terca or segunda == quarta or segunda == quinta or segunda == sexta:
    print("EMPATE !")
    semEmpate = False
elif terca == segunda or terca == quarta or terca == quinta or terca == sexta:
    print("EMPATE !")
    semEmpate = False
elif quarta == segunda or quarta == terca or quarta == quinta or quarta == sexta:
    print("EMPATE !")
    semEmpate = False
elif quinta == segunda or quinta == terca or quinta == quarta or quinta == sexta:
    print("EMPATE !")
    semEmpate = False
elif sexta == segunda or sexta == terca or sexta == quarta or sexta == quinta:
    print("EMPATE !")
    semEmpate = False

if(semEmpate):
    if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
        print("O dia escolhido foi segunda-feira com {} votos".format(segunda))
    elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
        print("O dia escolhido foi terça-feira com {} votos".format(terca))

    elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
        print("O dia escolhido foi terça-feira com {} votos".format(terca))

    elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
        print("O dia escolhido foi quarta-feira com {} votos".format(quarta))

    elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
        print("O dia escolhido foi quinta-feira com {} votos".format(quinta))

    elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
        print("O dia escolhido foi sexta-feira com {} votos".format(sexta))