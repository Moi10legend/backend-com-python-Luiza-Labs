from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    contador_clientes = 0
    def __init__(self, endereco = str):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    @property
    def contas(self):
        return self._contas

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
    numero_de_contas = 1
    def __init__(self, cliente = Cliente, numero = int):
        self._saldo = 0
        self._numero = numero
        self.agencia = "0002"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)
        
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
            print(f"Saque não efetuado, o valor é maior que o saldo de R${self.saldo}")
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

    def __str__(self):
        return f"""
Agência: {self.agencia}
C/C: {self.numero}     
Titular: {self.cliente.nome}         """
    
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
        return f"""
Agência: {self.agencia}
C/C: {self.numero}     
Titular: {self.cliente.nome}         """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            "Tipo": transacao.__class__.__name__,
            "Valor": transacao.valor,
            "Data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
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

def menu_inicial():
    menu = f"""
    Seja bem vindo ao aplicativo do banco!
    {datetime.now().strftime("%d/%m/%Y %H:%M")}
                      
        Escolha Uma das opções a seguir:
        [0] Sair do menu
        [1] Cadastrar novo usuário
    """
    return int(input(menu))

def menu():
    menu = f"""
    Seja bem vindo à sua conta bancária!
    {datetime.now().strftime("%d/%m/%Y %H:%M")}
                      
        Escolha Uma das opções a seguir:
        [0] Sair do menu
        [1] Depósito
        [2] Saque
        [3] Extrato
        [4] Cadastrar novo usuário
        [5] Criar nova conta
        [6] Listar as contas
    """
    return int(input(menu))

def main():
    usuarios = {}
    
    while True:
        if len(usuarios) == 0:
            opcao = menu_inicial()

            if opcao == 0:
                print("Muito obrigado por confiar em nós, até a próxima!")
                break
            elif opcao == 1:
                endereco = input("Digite o seu endereço: ")
                cpf = input("Digite o seu CPF: ") 
                nome = input("Digite o seu nome: ")
                data_nascimento = input("Digite a sua data de nascimento: ")
                usuarios[f"Usuário{Cliente.contador_clientes}"] = PessoaFisica(endereco, cpf, nome, data_nascimento)
                Cliente.contador_clientes += 1
                print("Usuário cadastrado com sucesso!")
            else:
                print("Opção inválida")

        else:
            opcao = menu()

            if opcao == 0:
                print("Muito obrigado por confiar em nós, até a próxima!")
                break

            if opcao == 1:
                cpf = input("Digite o CPF do seu usuário: ")

                for usuario in usuarios:
                    if usuarios[usuario].cpf == cpf:
                        print("Usuário encontrado!")
                        if len(usuarios[usuario].contas) == 0:
                            print("O usuário não possui contas, por favor crie uma")
                        else:
                            numero = int(input("Digite o número de sua conta: "))
                            for conta in usuarios[usuario].contas:
                                if numero == conta.numero:
                                    valor = float(input("Digite o valor que quer depositar: "))
                                    Deposito(valor).registrar(conta)
            
            if opcao == 2:
                cpf = input("Digite o CPF do seu usuário: ")

                for usuario in usuarios:
                    if usuarios[usuario].cpf == cpf:
                        print("Usuário encontrado!")
                        if len(usuarios[usuario].contas) == 0:
                            print("O usuário não possui contas, por favor crie uma")
                        else:
                            numero = int(input("Digite o número de sua conta: "))
                            for conta in usuarios[usuario].contas:
                                if numero == conta.numero:
                                    valor = float(input("Digite o valor que quer sacar: "))
                                    Saque(valor).registrar(conta)

            if opcao == 3:
                cpf = input("Digite o CPF do seu usuário: ")

                for usuario in usuarios:
                    if usuarios[usuario].cpf == cpf:
                        print("Usuário encontrado!")
                        if len(usuarios[usuario].contas) == 0:
                            print("O usuário não possui contas, por favor crie uma")
                        else:
                            numero = int(input("Digite o número de sua conta: "))
                            for conta in usuarios[usuario].contas:
                                if numero == conta.numero:
                                    for transacao in conta.historico.transacoes:
                                        print(transacao)

            if opcao == 4:
                endereco = input("Digite o seu endereço: ")
                cpf = input("Digite o seu CPF: ") 
                nome = input("Digite o seu nome: ")
                data_nascimento = input("Digite a sua data de nascimento: ")
                usuarios[f"Usuário{Cliente.contador_clientes}"] = PessoaFisica(endereco, cpf, nome, data_nascimento)
                Cliente.contador_clientes += 1
                print("Usuário cadastrado com sucesso!")

            if opcao == 5:
                cpf = input("Digite o CPF do seu usuário: ")

                for usuario in usuarios:
                    if usuarios[usuario].cpf == cpf:
                        print("Usuário encontrado!")
                        usuarios[usuario].adicionar_conta(Conta.nova_conta(usuarios[usuario], Conta.numero_de_contas))
                        Conta.numero_de_contas += 1
                        print("Conta criada com sucesso!")

            if opcao == 6:
                cpf = input("Digite o CPF do seu usuário: ")

                for usuario in usuarios:
                    if usuarios[usuario].cpf == cpf:
                        print("Usuário encontrado!")
                        for conta in usuarios[usuario].contas:
                            print(conta)

main()
                        
                        
        




    





