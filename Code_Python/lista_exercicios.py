# import random

# def valorPagamento(valor,atraso):
#     valorAtraso = 0
#     total = 0
#     if atraso == 0:
#         total = valor
#     else:
#         for day in range(atraso):
#             valorAtraso = valorAtraso + 1/100 * valor
#         total = valor + (3/100 * valor + valorAtraso)

#     return total

# valor = 1
# prestacoes = 0
# valorPrestacoes = 0
# while valor != 0:
#     valor = int(input("Qual o valor da prestacao\n"))
#     if valor == 0:
#         break
#     atraso = int(input("Quantos dias em atraso\n"))

#     print("O valor da prestacao é:", valorPagamento(valor,atraso))
#     prestacoes += 1
#     valorPrestacoes = valorPagamento(valor,atraso) + valorPrestacoes
    
# list_prestacoes = [prestacoes, valorPrestacoes]

# print(list_prestacoes)


#---------------------------------------------------------


# def somaImposto(custo):
#     taxaImposto = 1/10 * custo
#     custo = custo - taxaImposto
#     return custo

# x = int(input("Digite o valor do produto:"))

# print(somaImposto(x))


#---------------------------------------------------------

# dado1 = random.randrange(1,6)
# dado2 = random.randrange(1,6)

# totalDado = dado1 + dado2

# print(dado1, "\t",dado2, "\t", totalDado)
# checkpoint = 0

# if totalDado == 7 or totalDado == 11:
#     print('você ganhou')
# else:
#     if totalDado == 4 or totalDado == 5 or totalDado == 6 or totalDado == 8 or totalDado == 9 or totalDado == 10:
#         checkpoint = totalDado
#         while totalDado != checkpoint or totalDado != 7:
#             dado1 = random.randrange(1,6)
#             dado2 = random.randrange(1,6)
#             totalDado = dado1 + dado2
#             print(dado1, "\t",dado2, "\t", totalDado, "\t", checkpoint)
#             if totalDado == checkpoint:
#                 print('voce venceu')
#                 break
#             elif totalDado == 7:
#                 print('voce perdeu')
#                 break
#     else:
#         print('Voce perdeu')

            
            