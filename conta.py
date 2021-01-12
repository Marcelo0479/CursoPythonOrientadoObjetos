class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposito(self, valor):
        self.__saldo += valor

    def __saque_possível(self, valor_do_saque):
        valor_disponivel = self.__saldo + self.__limite
        return valor_do_saque <= valor_disponivel

    def saque(self, valor):
        if(self.__saque_possível(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} ultrapasou seu limite".format(valor))

    def trasferencia(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)

    @property
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

