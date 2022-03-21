class Tamagushi:
    def __init__(self,nome,fome,saude,idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def setNome(self,nome):
        self.nome = nome

    def setFome(self,fome):
        self.fome = fome

    def setSaude(self,saude):
        self.saude = saude

    def setIdade(self,idade):
        self.idade = idade

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def getSaude(self):
        return self.saude

    def getFome(self):
        return self.fome

    def humor(self):
        humor =  (float(self.fome) + float(self.saude)) /2
        return humor

def main():
    bixinho = Tamagushi('chato',5,2,1)




    
    

    

    