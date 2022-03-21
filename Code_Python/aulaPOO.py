
class Triangulo:
    def __init__(self,a,b,c):
        self.ladoa = a
        self.ladob = b
        self.ladoc = c

    def perimetro(self):
        perimetro = self.ladoa + self.ladob + self.ladoc
        return perimetro


    def tipo_lado(self):
        if self.ladoa == self.ladob:
            if self.ladoa == self.ladoc:
                return "equilátero"
            else:
                return "isósceles"
        elif self.ladoa == self.ladoc:
            return "isósceles"
        elif self.ladob == self.ladoc:
            return "isósceles"
        else:
            return "escaleno"
            

t = Triangulo(2,9,9)

perimetro = t.perimetro()

print(t.tipo_lado())


