class Ordenador:
    def bolha(self,lista):
        fim = len(lista)

        for i in range(fim-1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j],lista[j+1] = lista[j+1],lista[j]

    def bolha_melhorado(self,lista):
        fim = len(lista)

        for i in range(fim-1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j],lista[j+1] = lista[j+1],lista[j]
                    trocou = True
            if trocou == False :
                return 


               
          


o = Ordenador()

lista = [0,4,6,3,2]

o.bolha(lista)

print(lista)

