import random


dado1 = random.randrange(1,6)
dado2 = random.randrange(1,6)

dadosResultados = [4,5,6,8,9,10]

totalDado = dado1 + dado2

print(dado1, "\t",dado2, "\t", totalDado)
checkpoint = 0

if totalDado == 7 or totalDado == 11:
    print('você ganhou')
else:
    if totalDado in dadosResultados:
        checkpoint = totalDado
        while totalDado != checkpoint or totalDado != 7:
            dado1 = random.randrange(1,6)
            dado2 = random.randrange(1,6)
            totalDado = dado1 + dado2
            print(dado1, "\t",dado2, "\t", totalDado, "\t", checkpoint)
            if totalDado == checkpoint:
                print('voce venceu')
                break
            elif totalDado == 7:
                print('voce perdeu')
                break
    else:
        print('Voce perdeu')

            
            