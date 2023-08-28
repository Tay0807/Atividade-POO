class ContaBancaria:
    def __init__(self,titular,saldo,numero):
        self.titular = titular
        self.saldo = saldo
        self.numero = numero
    def depositar(self):
        deposito = float(input('Qual valor que irá depositar? '))
        self.saldo = self.saldo + deposito
    def saque(self):
        saque = float(input('Qual valor que irá sacar? '))
        self.saldo = self.saldo - saque
    def exibir(self):
        print('Seu novo saldo é: ', self.saldo)


banco_um = ContaBancaria('Tayna',1200,2022)
banco_um.saque()
banco_um.exibir()

banco_dois = ContaBancaria('Emyly',2200,2122)
banco_dois.depositar()
banco_dois.exibir()