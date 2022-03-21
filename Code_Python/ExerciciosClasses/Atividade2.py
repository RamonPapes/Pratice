
class quadrado:
    def __init__(self,lado):
        self.lado = lado


    def trocarLado(self):
        troca = input("Deseja trocar o lado? S/N\t")

        troca = troca[0].lower

        if troca == "s":
            novo_lado = input("Novo lado:")
            self.lado = novo_lado
        else:
            print("\n O lado continua " + self.lado)

    def mostrarLado(self):
        print("\n O tamanho do lado é " + self.lado)

    def calcularArea(self):
        area = int(self.lado) * int(self.lado)
        print("\n A area do quadrado é " + str(area))
    

def main():
    lado = input("Digite o valor do lado")
    quadrado1 = quadrado(lado)

    print(quadrado1)

    quadrado1.trocarLado()
    quadrado1.mostrarLado()
    quadrado1.calcularArea()

main()