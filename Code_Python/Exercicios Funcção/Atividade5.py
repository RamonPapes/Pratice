def somaImposto(custo):
    taxaImposto = 1/10 * custo
    custo = custo - taxaImposto
    return custo

x = int(input("Digite o valor do produto:"))

print(somaImposto(x))