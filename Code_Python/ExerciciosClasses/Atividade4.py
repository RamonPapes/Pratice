class Pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self,anos):
        if self.idade < 21:
            if self.idade + anos <= 21:
                self.altura = self.altura + (anos * 0.5)
            else:
                soma_altura = 0
                for i in range(self.idade,21):
                    soma_altura += 0.05
                self.altura += soma_altura

        self.idade += anos
        
    def mudarpeso(self,valor):
        self.peso += valor

    def crescer(self,valor):
        self.altura += valor


def main():
    ramon = Pessoa("Ramon", 20,62.0,1.70)

    print(ramon.altura)

    ramon.envelhecer(16)

    print("\n" + "A idade de ramon é: " + str(ramon.idade) + "\nE sua altura é: " + str(ramon.altura))



main()

    