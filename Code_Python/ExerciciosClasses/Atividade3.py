class Retangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def set_base(self,valor):
        self.base = valor
    
    def set_altura(self,valor):
        self.altura = valor

    def get_base(self):
        return self.base

    def get_altura(self):
        return self.altura

    def area(self):
        area = int(self.base) * int(self.altura)
        return area

    def perimetro(self):
        perimetro = int(self.base) * 2 + int(self.altura) * 2
        return perimetro
    

def main():
    base = int(input("Qual a base do retangulo: "))
    altura = int(input("Qual a altura do retangulo: "))

    local = Retangulo(base,altura)

    tamanho_piso = 2

    pisos = int(local.perimetro()) / tamanho_piso

    print("base do local: " + str(local.base) + "\n" + "Altura do local: " + str(local.altura))
    print("Perimetro do local " + str(local.perimetro()))
    print("\n serão necessários " + str(pisos) + " pisos")

main()
