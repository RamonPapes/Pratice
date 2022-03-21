class Conta:
    def __init__(self,numeroconta,nomecorrentista,saldo=0):
        self.numero = numeroconta
        self.proprietario = nomecorrentista
        self.saldo = saldo

    def alterar_nome(self,nome):
        self.proprietario = nome

    def deposito(self,valor):
        if valor > 0:
            self.saldo += valor
        else:
            return "Valor precisa ser positivo"

    def saque(self,valor):
        if valor > self.saldo:
            return "voce só pode sacar " + str(self.saldo)
        else:
            self.saldo -= valor


def main():
    conta1 = Conta(1424,"ramon")

    conta1.deposito(-10000)

    conta1.saque(15000)

    print("O saldo da conta é: " + str(conta1.saldo))

main()