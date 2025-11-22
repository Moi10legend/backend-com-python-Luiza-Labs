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

def mostrar_extrato(extrato):
    filtrar = input("""Só os depósitos[1]
Só os saques[2]
Todas as transações[3]: """)
    
    for transacao in geradortransacoes(filtrar, extrato):
        print(transacao)

extrato = {
    "Depósito": {
        "Depósito1": "avioan",
        "Depósito2": "anfi",
        "Depósito3": "Giga",
        "Depósito4": "an"
    },
    "Saques": {
        "Saque1": "Paraquai",
        "Saque2": "Bolívia",
        "Saque3": "Suriname",
        "Saque4": "Tailandia",
        "Saque5": "Groenlandia"
    }
}

mostrar_extrato(extrato)
