
AMorPM = ''
horario = ""
def convertHora(hora):
    if hora == 12:
        hora = 12

    elif hora >= 13:
        hora %= 12

    return hora

def PreouPos(hora):
    if hora >= 12:
        AMorPM = 'P'
    else:
        AMorPM = 'A'

    return AMorPM

def defHorario(hora,minuto):
    horario = str(hora) + ":" + str(minuto)

    return horario


count = ""
while count != "n" and count != "N":
    hora = int(input("Digite a hora atual \n"))
    minuto = int(input("Digite os minutos \n"))
    AMorPM = PreouPos(hora)

    hora = convertHora(hora)

    horario = defHorario(hora,minuto)

    print("A hora é " + horario + " " + AMorPM)
    count = str(input("Deseja continuar? S/N "))
    