
class bombaCombustivel:
    def init(self,tipo,valor,quantidade):
        self.tipo = tipo
        self.valorLitro = valor
        self.quantidade = quantidade

    def abastecerPorValor(self,valor):
        litros = int(valor / self.valorLitro)
        self.quantidade -= litros
        print("Foram colocados no veículo : " + str(litros) + " litros")

    def abastecerPorLitro(self,litros):
        valor = litros * int(self.valorLitro)
        print("Você deve pagar: " + str(valor))
        self.quantidade -= litros

    def setValor(self,valor):
        self.valorLitro = valor

    def alterarCombustivel(self,tipo):
        self.tipo = tipo

    def alteraQuantidade(self,quantidade):
        self.quantidade = quantidade

    def getQuantidade(self):
        return self.quantidade

    def getvalorLitro(self):
        return self.valorLitro

def main():
    bomba1 = bombaCombustivel("gasolina",10,100)

    bomba1.abastecerPorValor(50)

    bomba1.abastecerPorLitro(5)

    print(bomba1.getQuantidade())

main()