from pickle import APPEND
from readline import append_history_file


class Macaco:
    def init(self,nome):
        self.nome = nome
        self.bucho = [] 
        self.doenca_kuru = False

    def comer(self,alimento):
        self.bucho.append(alimento)
        if type(alimento) == Macaco():
            del alimento

    def verBucho(self):
        print(self.bucho)

    def digerir(self):
        self.bucho.pop()


def main():

    macaco1 = Macaco("Mamaco")
    macaco2 = Macaco("Comido")

    macaco1.comer()

    macaco1.verBucho()
    

main()