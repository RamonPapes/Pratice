class Carro:
    def init(self,consumo):
        self.consumo = consumo
        self.combustivel = 0

    def andar(self,distancia):
        self.combustivel -= (distancia / int(self.consumo))

    def getGasolina(self):
        print("Combustivel: " + str(self.combustivel))

    def abastecer(self,quantidade):
        if(quantidade > 0):
            self.combustivel += quantidade



def main():
    carro = Carro(20)

    carro.abastecer(20)
    carro.andar(100)
    carro.getGasolina()

main()