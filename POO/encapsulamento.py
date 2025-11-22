class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def getsaldo(self):
        print(f"O saldo na sua conta é de: {self._saldo}")

conta1 = Conta(1000)

conta1.sacar(200)
conta1.getsaldo()