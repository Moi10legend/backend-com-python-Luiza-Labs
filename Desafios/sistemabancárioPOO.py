from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco = str):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco=str, cpf = str, nome = str, data_nascimento = str):
        super().__init__(endereco)
        self._cpf = cpf
        self.nome = nome
        self._data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self._cpf
    
    @property
    def data_nascimento(self):
        return self._data_nascimento

class Conta:
    def __init__(self, numero = int, cliente = Cliente):
        self._saldo = 0
        self._numero = numero
        self.agencia = "0002"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
        
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo = self._saldo - valor
            print("Saque realizado com sucesso!")
            return True
        elif valor > self._saldo:
            print("Saque não efetuado, o valor é maior que o saldo")
        else:
            print("Valor inválido")

        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
            return True
        else:
            print("Valor inserido é inválido")
        
        return False
    
class ContaCorrente(Conta):
    def __init__(self, limite = 500, limite_saques = 3):
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes
                             if transacao['Tipo'] == Saque.__name__ ])
        
        if valor > self.limite:
            print("A operação falhou, o valor é maior que o limite para saque")
        elif numero_saques >= self.limite_saques:
            print("Operação falhou, o limite de saques foi atingido")
        else:
            return super().sacar(valor)

        return False
    
    def __str__(self):
        print(f"""
Agência: {self.agencia}
C/C: {self.numero}     
Titular: {self.cliente.nome}         """)


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "Tipo": transacao.__class__.__name__,
            "Valor": transacao.valor,
            "Data": datetime.now().strftime("%d/%mm/%YYYY %HH:%MM:%s")
        })

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)



    





