def valorPagamento(valor,atraso):
    valorAtraso = 0
    total = 0
    if atraso == 0:
        total = valor
    else:
        for day in range(atraso):
            valorAtraso = valorAtraso + 1/100 * valor
        total = valor + (3/100 * valor + valorAtraso)

    return total

valor = 1
prestacoes = 0
valorPrestacoes = 0
while valor != 0:
    valor = int(input("Qual o valor da prestacao\n"))
    if valor == 0:
        break
    atraso = int(input("Quantos dias em atraso\n"))

    print("O valor da prestacao é:", valorPagamento(valor,atraso))
    prestacoes += 1
    valorPrestacoes = valorPagamento(valor,atraso) + valorPrestacoes
    
list_prestacoes = [prestacoes, valorPrestacoes]

print(list_prestacoes)