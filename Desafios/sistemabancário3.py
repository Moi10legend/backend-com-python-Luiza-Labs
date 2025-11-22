from datetime import datetime
import functools

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

def geradortransacoes(filtrar, extrato):

    match filtrar:
        case "1":  # só depósitos
            for chave, dados in extrato.items():
                if chave == "Depósito":
                    for nome, valor in dados.items():
                        yield valor

        case "2":  # só saques
            for chave, dados in extrato.items():
                if chave == "Saques":
                    for nome, valor in dados.items():
                        yield valor

        case "3":  # tudo
            for chave, dados in extrato.items():
                for nome, valor in dados.items():
                    yield valor

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        resultado = funcao(*args, **kwargs)
        print(f"A operação {funcao.__name__} foi realizada às {datetime.now().strftime("%d/%m/%Y %H:%M")}")
        return resultado
    return envelope

@meu_decorador
def depositar(valor, saldo, extrato, data_ultima_transacao: datetime, data_atual: datetime, quantidade_transacoes_realizadas, contador_depositos):
    if quantidade_transacoes_realizadas < 10 or (quantidade_transacoes_realizadas == 10 and data_ultima_transacao.strftime("%d/%m/%Y") != data_atual.strftime("%d/%m/%Y")):
        saldo += valor
        extrato["Depósito"][f"Depósito{contador_depositos}"] = f"Depósito de R${valor} foi realizado às {datetime.now().strftime("%d/%m/%Y %H:%M")} \n"
        quantidade_transacoes_realizadas += 1
        contador_depositos += 1
        print("Depósito realizado com sucesso!")
        return saldo, extrato, data_ultima_transacao, quantidade_transacoes_realizadas, contador_depositos
    else:
        print("A quantidade de trasações diárias já foi atingida (10)")
        return saldo, extrato, data_ultima_transacao, quantidade_transacoes_realizadas
        
@meu_decorador
def sacar(valor, saldo, extrato, data_atual: datetime, data_ultima_trasacao: datetime, quantidade_transacoes_realizadas, contador_saques):
    if quantidade_transacoes_realizadas < 10 or (quantidade_transacoes_realizadas == 10 and data_ultima_trasacao.strftime("%d/%m/%Y") != data_atual.strftime("%d/%m/%Y")) or data_ultima_trasacao == None:
        if saldo >= valor:
            saldo -= valor
            data_ultima_trasacao = data_atual
            extrato["Saque"][f"Saque{contador_saques}"]= f"Saque de R${valor} foi realizado às {data_atual.strftime("%d/%m/%Y %H:%M")} \n"
            quantidade_transacoes_realizadas += 1
            contador_saques += 1
            print("Saque realizado com sucesso!")
            return saldo, extrato, data_ultima_trasacao, quantidade_transacoes_realizadas, contador_saques
        else:
            print(f"O valor desejado é maior que o saldo atual de R${saldo}")
            return saldo, extrato, data_ultima_trasacao, quantidade_transacoes_realizadas, contador_saques
    else:
        print("A quantidade de trasações diárias já foi atingida (10)")
        return saldo, extrato, data_ultima_trasacao, quantidade_transacoes_realizadas, contador_saques

def mostrar_extrato(extrato):
    filtrar = input("""Só os depositos[1]
Só os saques[2]
Todas as transações[3]: """)
    for transacao in geradortransacoes(filtrar, extrato):
        print(transacao)

@meu_decorador
def cadastrar_novo_usuario(usuarios, contador_usuario):
    cpf_novo_usuario = int(input("Digite o CPF do novo usuário (somente números): "))

    for usuario in usuarios:
        if usuarios[usuario]['CPF'] == cpf_novo_usuario:
            print("O CPF digitado já possui usuário!")
            break
        
    nome = input("Digite o nome completo do usuário: ")   
    data_nascimento = input("Digite sua data de nascimento (dd/mm/yyyy): ")
    endereco = input("Digite o endereço (Rua, nº - Bairro - Cidade/UF): ")
    usuarios[contador_usuario] = {"CPF": cpf_novo_usuario, "nome": nome, "data_nascimento": data_nascimento, "endereço": endereco}
    print("Novo usuário cadastrado!")
    contador_usuario += 1
    return contador_usuario

def criar_nova_conta(agencia, numero_conta, contas, usuarios):
    cpf = int(input("Digite o CPF do usuário (somente números): "))
    tem_usuario = False

    for usuario in usuarios:
        if usuarios[usuario]['CPF'] == cpf:
            contas.append({"agência": agencia, "Número da conta": numero_conta, "Usuário": usuarios[usuario]})
            tem_usuario = True
            numero_conta += 1
            print("Conta cadastrada com sucesso!")
            return numero_conta
    
    if tem_usuario == False:
        print("O CPF inserido não está cadastrado")
        

def listar_contas(contas):
    cpf = int(input("Digite o CPF do usuário (somente números): "))
    tem_conta = False

    for conta in contas:
        if conta["Usuário"]["CPF"] == cpf:
            tem_conta = True
            print(conta)
            print()
    
    if tem_conta == False:
        print("Não existe conta pertencente a este usuário")

def main():
    saldo = 0
    extrato = {"Depósito": {},
               "Saque": {}}
    data_atual = datetime.now()
    data_ultima_transacao = None
    quantidade_de_transacoes_realizadas = 0
    usuarios = {}
    contador_usuarios = 1
    contador_saques = 0
    contador_depositos = 0
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == 0:
            print("Muito obrigado por confiar em nós, até a próxima!")
            break
        elif opcao == 1:
            valor = float(input("Digite o valor a ser depositado: "))
            saldo, extrato, data_ultima_transacao, quantidade_de_transacoes_realizadas, contador_depositos = depositar(valor, saldo, extrato, data_ultima_transacao, data_atual, quantidade_de_transacoes_realizadas, contador_depositos)
        elif opcao == 2:
            valor = float(input("Digite o valor a ser sacado: "))
            saldo, extrato, data_ultima_transacao, quantidade_de_transacoes_realizadas, contador_saques = sacar(valor, saldo, extrato, data_atual, data_ultima_transacao, quantidade_de_transacoes_realizadas, contador_saques)
        elif opcao == 3:
            mostrar_extrato(extrato)
        elif opcao == 4:
            contador_usuarios = cadastrar_novo_usuario(usuarios, contador_usuarios)
        elif opcao == 5:
            numero_conta = criar_nova_conta(31, numero_conta, contas, usuarios)
        elif opcao == 6:
            listar_contas(contas)
            
    if data_ultima_transacao != None:
        if data_ultima_transacao.strftime("%d/%m/%Y") != data_atual.strftime("%d/%m/%Y"):
            quantidade_de_transacoes_realizadas = 0
    
main()

