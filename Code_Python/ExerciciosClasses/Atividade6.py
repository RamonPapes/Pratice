class TV:
    def __init__(self,volume=0,canal=0):
        self.volume = volume
        self.canal = canal

    def setCanal(self,canal):
        if canal > 0 and canal<=15:
            self.canal = canal

    def setVolume(self,volume):
        if volume >=0 and volume <=10:
            self.volume = volume


def main():
    tv = TV()

    tv.setCanal(3)

    tv.setVolume(10)

    print("O canal da Tv é: " + str(tv.canal) + "O volume da Tv é: " + str(tv.volume))



