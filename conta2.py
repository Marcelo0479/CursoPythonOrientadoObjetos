class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("contruindo...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def deposito(self, valor):
        self.__saldo += valor

    def __saque_disponivel(self, valor_do_saque):
        valor_disponivel = self.__saldo + self.__limite
        return valor_do_saque <= valor_disponivel

    def saque(self, valor):
        if(self.__saque_disponivel(valor)):
            self.__saldo -= valor
        else:
            print("O valor R${} ultrapassou seu limite".format(valor))

    def extrato(self):
        print("O saldo do {} é de R${}".format(self.__titular, self.__saldo))

    def transferencia(self, valor, destino):
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
    def codigo_bancario():
        return "001"
